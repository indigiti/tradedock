[← English documentation](README.md)

# Getting started

## First launch

Trading Hub starts with a **simulated account**, so using it for the first time does not send live orders to a broker. You can open simulated instruments without adding credentials. Real trading requires an explicit connection and permission to send real orders.

## Main navigation

- **Trading**: chart workspace, order book, tape, drawings, and manual trading.
- **Account**: balances, open positions, orders, executions, trades, and statistics.
- **Backtesting**: write or select a C# strategy, test it, optimize it, and create reports.
- **Live**: supervise running strategies, portfolios, market conditions, and risk proposals.
- **Data**: inspect local historical data, download supported history, and import CSV files.
- **Connections**: configure the simulated feed, exchanges, brokers, and historical providers.
- **Settings**: appearance, time zone, order confirmation, hotkeys, recordings, and sleep behavior.

On macOS, shortcuts use the Command key. For example, **Command-1** opens Trading, **Command-2** Backtesting, **Command-3** Data, **Command-4** Connections, and **Command-5** Account. See Settings for other shortcuts.

## Open a chart

1. Select the Trading section.
2. Open the instrument picker and choose the simulated feed or a configured exchange.
3. Choose a symbol, timeframe, and chart style.
4. Switch among candles, footprint, and other chart representations as needed.
5. Open Chart Trader or DOM only after confirming the selected account.

A newly opened chart can load locally recorded ticks first, then request additional history from its connection. Opening more tabs or selecting a multi-chart layout does not automatically enable real orders.

## Practice before trading

In Chart Trader, ensure the selected account is **Simulated**. Try a market or limit order, inspect order history and the position, add a stop and a target, and close the simulated position. Check the Account page and learn how order cancellation and reversal work.

## macOS menu bar behavior

By default, closing the application window can keep Trading Hub running in the menu bar, including live strategy activity. To stop the program completely, use **Command-Q** or the menu-bar Quit action.

## Next steps

Review [Connections](conexiones.md), [Charts](graficos.md), and [Trading](operar.md). For automated experiments, read [Strategies](estrategias.md) and [Backtesting](backtesting.md). For real account operations, read the [risk safeguards](operar.md#real-money-safeguards).
