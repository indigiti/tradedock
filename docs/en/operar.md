[← English documentation](README.md)

# Manual trading

Trade through **Trading**, using Chart Trader, DOM (Depth of Market), chart context menus, or configured hotkeys. Each chart remembers its **own selected account**. The initial selection is the simulated account.

## Account selection

The simulated account works with any supported chart. Broker accounts depend on connection and instrument compatibility: Binance charts may offer the corresponding Binance testnet/real account; Rithmic charts may offer Rithmic paper/real; CME futures charts from Rithmic or Tradovate may offer Tradovate demo/real. Real account selection is clearly highlighted.

## Chart Trader

Chart Trader appears beside an individual chart and in the panel above the DOM for the active chart. It offers:

| Control | Action |
|---|---|
| Account | Choose execution destination |
| Quantity and quick sizes | Select order size |
| Buy MKT / Sell MKT | Submit a market order |
| Buy Ask / Sell Ask | Submit a limit order at the current ask |
| Buy Bid / Sell Bid | Submit a limit order at the current bid |
| Cancel buys / Cancel sells / Cancel all | Cancel outstanding orders |
| Reverse | Reverse an existing position |
| Breakeven | Move a protective stop to entry price |
| Close 25% / 50% / 75% | Partial close at market |
| Close position | Close position and cancel related orders |
| Auto SL / TP | Apply stop-loss and take-profit template |

The right-side DOM execution controls use the active chart's account and quantity.

## Order types and simulation

- **Market:** fill at the available best bid/ask in the simulated book, falling back to last price if necessary.
- **Limit:** fill at or through a specified price, with a simulated queue model.
- **Stop:** trigger when the specified price trades, then execute as a market order.
- **Bracket/OCO:** protective stop and targets must reduce, never enlarge or reverse, an existing position.

These simulation rules are not a guarantee of actual broker execution.

## Trading through the DOM

Click the bid column to enter a buy order; click the ask column for a sell. A price at/through the opposite side may become a stop according to the DOM action. Right-click or Option-click a price to cancel your orders there. Drag an order to amend its price. Recenter or scroll the ladder as needed.

When the **Double-click to trade** setting is enabled in DOM preferences, ordinary single clicks do not submit orders; cancellation remains accessible.

## Trading from the chart

Right-click a price for context-sensitive buy/sell limit or stop orders, drag order lines to amend price, or right-click an existing order to cancel it. When in a position, use the chart menu for a partial/full close, breakeven, or protective orders. Review account and price before interacting with lines.

## Stops and profit targets

In **Auto SL / TP**, enable a stop distance in ticks and one or more target distances. Up to three partial targets can distribute the position's total size. Optional **Breakeven at TP1** moves the stop to entry when the first target fills. Applying the template to an open position replaces its current stop and targets; increasing or reducing position size adjusts protection.

## Cross trading

Display one contract and route orders to another compatible contract, such as ES for analysis and MES for execution. The order, stop, and targets are sent with the **specified numerical prices**; the platform warns when the symbols' prices differ. Be certain that tick sizes and quoted prices are suitable for the routed instrument.

## Hotkeys and account history

Configure manual trading shortcuts under **Settings → Keyboard shortcuts → Trading**. They are unassigned by default. **Account** (**Command-5**) shows balance, daily PnL, open PnL, orders, fills, closed trades, and period-based performance statistics. The simulated account can be reset only with no live simulated positions or orders; previous history is retained separately.

## Real-money safeguards

- Live orders are disabled for each connection until explicitly authorized.
- Simulated, paper, demo, and testnet accounts do not prompt before each order.
- Real accounts may require confirmations for submissions, modifications, closures, reversal, and cancellations; settings vary by provider.
- A configured maximum order quantity blocks oversize live orders.
- Automated strategies have daily loss/drawdown controls and a **Stop all** facility to cancel orders and close related positions.
- The Chart Trader and Account screen prominently identify real accounts.

**Always inspect the actual order confirmation, provider entitlement, and position state.** Never interpret backtest or simulator fills as proof of real execution behavior.
