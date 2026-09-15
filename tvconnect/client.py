"""Client for pulling market data and technical analysis from TradingView."""

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional

from tradingview_ta import Interval, TA_Handler

_INTERVAL_ALIASES = {
    "1m": Interval.INTERVAL_1_MINUTE,
    "5m": Interval.INTERVAL_5_MINUTES,
    "15m": Interval.INTERVAL_15_MINUTES,
    "30m": Interval.INTERVAL_30_MINUTES,
    "1h": Interval.INTERVAL_1_HOUR,
    "2h": Interval.INTERVAL_2_HOURS,
    "4h": Interval.INTERVAL_4_HOURS,
    "1d": Interval.INTERVAL_1_DAY,
    "1w": Interval.INTERVAL_1_WEEK,
    "1mo": Interval.INTERVAL_1_MONTH,
}


class TradingViewError(RuntimeError):
    """Raised when TradingView data cannot be fetched or a symbol is unknown."""


@dataclass
class Quote:
    """A single symbol's technical analysis snapshot from TradingView."""

    symbol: str
    exchange: str
    screener: str
    interval: str
    summary: Dict[str, Any]
    oscillators: Dict[str, Any]
    moving_averages: Dict[str, Any]
    indicators: Dict[str, Any] = field(repr=False)

    @property
    def price(self) -> Optional[float]:
        return self.indicators.get("close")

    @property
    def recommendation(self) -> Optional[str]:
        return self.summary.get("RECOMMENDATION")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "symbol": self.symbol,
            "exchange": self.exchange,
            "screener": self.screener,
            "interval": self.interval,
            "price": self.price,
            "recommendation": self.recommendation,
            "summary": self.summary,
            "oscillators": self.oscillators,
            "moving_averages": self.moving_averages,
        }


def _resolve_interval(interval: str) -> str:
    try:
        return _INTERVAL_ALIASES[interval.lower()]
    except KeyError:
        valid = ", ".join(sorted(_INTERVAL_ALIASES))
        raise TradingViewError(
            f"Unknown interval {interval!r}. Valid options: {valid}"
        ) from None


class TradingViewClient:
    """Thin wrapper around tradingview-ta for fetching quotes and indicators.

    Talks directly to TradingView's public scanner API (no account or API key
    required). Requires outbound HTTPS access to scanner.tradingview.com.
    """

    def __init__(self, screener: str = "america", exchange: str = "NASDAQ", interval: str = "1d"):
        self.screener = screener
        self.exchange = exchange
        self.interval = interval

    def get_quote(
        self,
        symbol: str,
        exchange: Optional[str] = None,
        screener: Optional[str] = None,
        interval: Optional[str] = None,
    ) -> Quote:
        """Fetch a technical-analysis snapshot for a single symbol."""

        exchange = exchange or self.exchange
        screener = screener or self.screener
        interval = interval or self.interval

        handler = TA_Handler(
            symbol=symbol,
            exchange=exchange,
            screener=screener,
            interval=_resolve_interval(interval),
        )

        try:
            analysis = handler.get_analysis()
        except Exception as exc:  # tradingview_ta raises plain Exception
            raise TradingViewError(
                f"Failed to fetch {exchange}:{symbol} ({screener}, {interval}): {exc}"
            ) from exc

        return Quote(
            symbol=symbol,
            exchange=exchange,
            screener=screener,
            interval=interval,
            summary=analysis.summary,
            oscillators=analysis.oscillators,
            moving_averages=analysis.moving_averages,
            indicators=analysis.indicators,
        )

    def get_quotes(
        self,
        symbols: Iterable[str],
        exchange: Optional[str] = None,
        screener: Optional[str] = None,
        interval: Optional[str] = None,
    ) -> List[Quote]:
        """Fetch technical-analysis snapshots for multiple symbols.

        Raises TradingViewError on the first symbol that fails; call
        get_quote directly if you need per-symbol error handling instead.
        """

        return [
            self.get_quote(symbol, exchange=exchange, screener=screener, interval=interval)
            for symbol in symbols
        ]
