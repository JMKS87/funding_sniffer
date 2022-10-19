from decimal import Decimal

import pytest

from fetch_fundings import fetch_fundings, Funding


@pytest.mark.it
def test_funding_integration():
    #given
    expected_exchanges = {'HuobiDM', 'BitMEX', 'FTX', 'Bybit', 'OKX', 'Deribit', 'Kraken', 'Binance'}
    expected_fundings = 14  # subject to change, non-essential

    #when
    fundings = fetch_fundings()

    #then
    assert fundings
    assert isinstance(fundings, list)
    assert len(fundings) == expected_fundings
    exchanges = set()
    for funding in fundings:
        ticker = funding.ticker
        exchanges.add(ticker)
        assert isinstance(funding, Funding)
        assert isinstance(ticker, str)
        # Deribit seems to not provide predicted funding
        is_deribit = ticker == "Deribit"
        if not is_deribit:
            assert isinstance(funding.funding, Decimal)
    assert exchanges == expected_exchanges
