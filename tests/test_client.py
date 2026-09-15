from unittest.mock import MagicMock, patch

import pytest

from tvconnect.client import TradingViewClient, TradingViewError, _resolve_interval


def _fake_analysis():
    analysis = MagicMock()
    analysis.summary = {"RECOMMENDATION": "BUY", "BUY": 10, "SELL": 2, "NEUTRAL": 5}
    analysis.oscillators = {"RECOMMENDATION": "NEUTRAL"}
    analysis.moving_averages = {"RECOMMENDATION": "BUY"}
    analysis.indicators = {"close": 123.45, "RSI": 55.5}
    return analysis


def test_resolve_interval_known():
    assert _resolve_interval("1d") is not None
    assert _resolve_interval("1D") == _resolve_interval("1d")


def test_resolve_interval_unknown():
    with pytest.raises(TradingViewError):
        _resolve_interval("banana")


@patch("tvconnect.client.TA_Handler")
def test_get_quote(mock_handler_cls):
    mock_handler_cls.return_value.get_analysis.return_value = _fake_analysis()

    client = TradingViewClient(screener="america", exchange="NASDAQ", interval="1d")
    quote = client.get_quote("AAPL")

    assert quote.symbol == "AAPL"
    assert quote.exchange == "NASDAQ"
    assert quote.price == 123.45
    assert quote.recommendation == "BUY"
    assert "indicators" not in quote.to_dict()
    mock_handler_cls.assert_called_once()


@patch("tvconnect.client.TA_Handler")
def test_get_quote_wraps_errors(mock_handler_cls):
    mock_handler_cls.return_value.get_analysis.side_effect = Exception("boom")

    client = TradingViewClient()
    with pytest.raises(TradingViewError, match="boom"):
        client.get_quote("AAPL")


@patch("tvconnect.client.TA_Handler")
def test_get_quotes_multiple(mock_handler_cls):
    mock_handler_cls.return_value.get_analysis.return_value = _fake_analysis()

    client = TradingViewClient()
    quotes = client.get_quotes(["AAPL", "MSFT"])

    assert [q.symbol for q in quotes] == ["AAPL", "MSFT"]
    assert mock_handler_cls.call_count == 2
