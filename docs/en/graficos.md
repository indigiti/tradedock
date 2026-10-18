[← English documentation](README.md)

# Charts

The Trading workspace can show one or several charts in a tab. A chart combines an instrument, data connection, selected timeframe, styling, overlays, and optional trading tools.

## Toolbar and market history

Use the chart toolbar to choose an instrument and timeframe, switch drawing/indicator controls, and access chart appearance, templates, footprint settings, DOM, and tape. Recorded ticks and downloaded candles are loaded from local storage first. Missing intervals can be requested from the current data connection.

## Bar periods and chart styles

Trading Hub supports time-based, tick-count, traded-volume, and range-based bars. Display options include candlesticks, OHLC bars, lines, and Heikin Ashi. A tick-based or footprint chart needs appropriately granular underlying trade history; coarse candle history cannot reproduce actual bid/ask executions.

## Footprint

Footprint displays activity inside each price level and bar. Configure columns such as bid/ask volume, delta, total volume, point of control (POC), and per-candle volume profile. Use the footprint editor to control column order, colors, cell borders, and related presentation settings.

## Navigate and arrange charts

Scroll and drag to inspect previous data, zoom time and price, and return to the newest live price when needed. Multiple layouts are available, including one chart, two side-by-side, two stacked, and one large chart with two small charts. A chart can be detached to a separate window/monitor. Color-linked chart groups can synchronize compatible navigation or instrument changes.

## Drawings, indicators, and templates

Add trend lines and other drawing tools from the chart menus. Indicators include moving averages, VWAP, Bollinger Bands, RSI, MACD, volume, delta, CVD, session profile, and large trades. Create chart templates to save presentation, indicators, footprint columns, and colors without binding to a specific symbol or timeframe.

## DOM, tape, and profile

DOM shows the order book at price levels. Trade tape lists executions, and a volume profile summarizes market activity by price. These depend on the selected feed; quote-only markets cannot provide exchange-grade aggressive-side trade volume.

## Replay

Select a previously recorded trading day in Data and open it as a replay. Review the market at different speeds and practice with the simulated trading account. Replay should not access your actual live brokerage account.

## Strategies on charts

A compatible compiled C# strategy can be inspected or launched from a chart, with position and historical backtest context. Review symbol, timeframe, market data, selected trading account, and safety limits before launching any live strategy.

For order controls and protective exits, read [Manual trading](operar.md).
