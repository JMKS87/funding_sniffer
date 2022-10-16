import json
import logging
import os
import time
from datetime import datetime
from decimal import Decimal
from typing import List

from config import setup_logging, DATA_DIR, FETCH_INTERVAL
from fetch_fundings import fetch_fundings, Funding

logger = logging.getLogger(__name__)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def write_fundings(fundings: List[Funding]) -> None:
    data = {
        "timestamp": int(time.time()),
        "fundings": [(funding.ticker, funding.funding) for funding in fundings]
            }

    today = datetime.today().strftime('%Y-%m-%d')
    filename = os.path.join(DATA_DIR, f"fundings_{today}.log")
    with open(filename, "a") as ouf:
        ouf.write(json.dumps(data, cls=DecimalEncoder) + "\n")
    logger.info("Saved fundings!")

def fetch_fundings_cron(interval: int) -> None:
    while True:
        try:
            fundings = fetch_fundings()
            write_fundings(fundings)
        except Exception:
            logger.exception("Exception during funding collection!")
        time.sleep(interval)


if __name__ == "__main__":
    setup_logging()
    fetch_fundings_cron(FETCH_INTERVAL)
