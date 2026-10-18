[← English documentation](README.md)

# Market data and historical downloads

The Data screen shows market data recorded on your computer and enables historical downloads, imports, cleanup, and replay.

## Where chart history comes from

1. Existing local trade-by-trade recordings.
2. Existing downloaded provider history and candles.
3. An enabled market-data connection queried for missing history.

When opening a chart, data already stored locally is available immediately. Tick history preserves more execution detail than coarse OHLC candles, which matters for footprint, DOM analysis, and detailed backtesting.

## Stored days and replay

Select a connection/instrument and inspect the stored trading days and approximate relative file sizes. Select one or multiple days to delete only when sure they are no longer needed. Deleted local history cannot be reconstructed without downloading it again. Open a recorded day as a simulated replay in Trading.

## Download history

Choose a supported instrument and an available time range, then request history from its provider. Rithmic, crypto feeds, and other supported connections may expose different datasets and maximum lookback periods. Daily downloads can be interrupted and resumed; previously saved days remain available. Some gaps represent exchange holidays, weekends, or unpublished sessions rather than errors.

## CSV import

Historical CSV or TXT exports from Dukascopy, HistData, MetaTrader, TradingView, and other compatible formats can be imported. Select symbol and time-zone interpretation carefully. Review the resulting row count, unreadable-line count, and recorded dates before trusting the data in strategies.

## Databento

Databento delivers historical CME futures trade-level data including aggressor side. It is billed by usage and **must not download automatically without cost review**. Configure a Databento key in Connections, choose the futures product and date range in Data, calculate the estimated download charge, and confirm before downloading. Databento history is stored separately and can be selected alone or combined with Rithmic data. Where both cover a day, the combined option prioritizes Rithmic and fills missing coverage from Databento.

## Data integrity

Check time zones, symbol/contract rollovers, duplicate sessions, missing ticks, stale records, and differences between recorded trades and broker-reported aggregates. Backtesting results are not meaningful without adequate history and sound fill assumptions. Never let automated tests write into your live account or tick folders.

See [Backtesting](backtesting.md) and [Privacy](privacidad.md).
