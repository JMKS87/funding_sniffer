import string
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import List, Optional

import requests
from bs4 import BeautifulSoup

WHITESPACE_CHARS = string.whitespace + "\xa0"

@dataclass
class Funding:
    ticker: str
    funding: Optional[Decimal]

    @classmethod
    def from_coinalyze_html(cls, ticker: str, raw_value: str) -> "Funding":
        try:
            funding = Decimal(raw_value.strip(WHITESPACE_CHARS).rstrip("%")) / 100
        except InvalidOperation:
            funding = None
        return cls(ticker=ticker, funding=funding)


def fetch_fundings() -> List[Funding]:
    fundings = []
    response = requests.get("https://coinalyze.net/bitcoin/funding-rate/")
    soup = BeautifulSoup(response.text, "lxml")
    funding_table = soup.find("table", {"class": "funding-rates"})
    boxes = funding_table.findAll("div", {"class": "box"})
    for box in boxes:
        name = box.find("div", {"class": "box-title"})
        values = box.findAll("div", {"class": "box-row"})
        if not name.text.strip(WHITESPACE_CHARS):
            continue
        funding = Funding.from_coinalyze_html(ticker=name.text, raw_value=values[1].text)
        # print(name.text, [value.text for value in values])
        # print(funding)
        fundings.append(funding)
    return fundings


if __name__ == "__main__":
    print(fetch_fundings())
