[← English documentation](README.md)

# Live strategy execution

**Live** shows running strategies, market conditions, portfolios, completed trades, and risk proposals. A live strategy can use a simulated, demo/testnet, or explicitly authorized real brokerage account.

## Account readiness

Verify the account, contract, enabled data connection, exchange session, permission to submit orders, current positions, and order limits. The simulator is the recommended default. A real account should be clearly labeled; do not infer the account from the displayed market symbol alone.

## Launch a strategy

Launch from Backtesting, the Live section, or a chart. Select a compiled strategy and inspect its settings. Choose the account and position size, then set a maximum daily loss and drawdown. Review existing orders and exposure before enabling automation. Test first with simulation.

## Position size and smart contracts

Set an explicit quantity or use the supported contract-sizing controls. For products with micro and mini contracts, inspect which contract is actually selected and its monetary tick value. The chosen size must fit buying power and risk limits.

## Risk limits

A strategy can pause or stop on configured loss or drawdown limits. The global **Stop all / Kill switch** stops running strategies, cancels related orders, and attempts to close their positions. This action is operationally sensitive: verify resulting broker state and check for outstanding fills or failed cancellations.

## Live dashboard

Strategy rows summarize account, instrument, position, size, current/closed PnL, loss/drawdown thresholds, and execution state. Inspect the detail pane before modifying risk parameters, pausing, stopping, or removing a strategy. The Trades view displays completed trades and metrics such as MAE/MFE.

## Portfolios

Group strategies to review combined risk, concentration, historical performance, correlations, and live results. Portfolios can use rule-based or Claude-assisted sizing suggestions. These are proposed adjustments, not a substitute for margin checks or broker-side controls.

## Risk proposals

The rule-based helper can suggest increasing size for stronger recent results or reducing/pausing poorly performing strategies. Claude can analyze portfolio context and propose changes. Review every proposal. **Real-account sizing proposals require explicit approval.**

## Market conditions

The Market view classifies broad market behavior, such as trend/range and volatility, to help assess which strategies fit the current environment. Regime detection is probabilistic and can change.

## Closing and restarting the app

Closing the macOS main window may keep the app running in the menu bar. The application can optionally resume live strategies on launch. **Automatic restart for real-money strategies is disabled by default.** Explicitly verify any restart preference and use Command-Q to quit completely.

## Incident checks

If data is stale, a provider disconnects, orders are rejected, an execution acknowledgment is missing, or PnL diverges, stop or pause automation as appropriate and reconcile the actual account at the broker. Do not rely solely on local charts or notifications.
