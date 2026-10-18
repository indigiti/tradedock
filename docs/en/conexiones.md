[← English documentation](README.md)

# Connections

In **Connections** (**Command-4**), select where chart data comes from and which accounts may send orders.

## Add and test a connection

1. Choose **New connection** and select the provider.
2. Complete the provider-specific fields.
3. Click **Test connection**; this saves the configuration and tests connectivity.
4. Use **Save** after subsequent changes.
5. Enable or disable a connection with its toggle. Disabled connections do not offer market symbols or trading accounts.

The connection list shows whether each provider is disabled, untested, connected, or failed. Many providers support a configurable history-on-open duration, from approximately 30 minutes to 7 days. Recorded data loads first; missing data may be retrieved from the provider.

## Credential storage

Passwords, private API secrets, tokens, and the Databento key are stored in **macOS Keychain**, not in plaintext files. `connections.json` keeps connection names, usernames, servers, public key identifiers, and settings. A saved secret field appears masked. Leaving that field blank when editing retains the stored secret; typing a replacement updates it. Removing a connection also removes its Keychain secrets, but not historical market data.

## Provider comparison

| Provider | Data and market | Can place orders? |
|---|---|---|
| Simulator | Offline simulated order book; SIM-BTC, SIM-ETH, SIM-ES, SIM-NQ | Simulation only |
| Binance Futures / Spot | Public cryptocurrency data and history | Testnet or real when configured |
| Bybit | Public USDT perpetuals | No; data only |
| Rithmic | CME futures data, history, and accounts | Paper or real, with permission |
| AMP Futures | Rithmic-backed CME futures connection | Paper or real, with permission |
| Tradovate | CME futures data and accounts | Demo or real, with permission |
| cTrader | Broker forex/CFD data | No; data only |
| OANDA | Forex, indices, gold, and CFDs | No; data only |
| Alpaca | US stocks/ETF market data | No; data only |
| Databento | Paid, historical CME futures ticks | No; historical data only |
| Interactive Brokers | TWS / IB Gateway connection test | Not yet; no market data or orders |

Any supported feed can be observed using a simulated trading account.

## Binance

Market data is public, so API credentials are unnecessary for charts, DOM, tape, or history. To trade, select **Testnet** (default) or **Real account**, provide API key and secret, and create keys **without withdrawal permission**. Real orders require an additional **Allow REAL orders** checkbox. Optional safeguards include a real-order confirmation and maximum order size.

## Rithmic and AMP Futures

Provide the account username, password, and server/system. The provider list is fetched with latency estimates; a custom `wss://` address may be entered when necessary. Default timeout is 10,000 milliseconds. Rithmic can offer aggregated order-book updates when supported by the chosen system. Some systems require an approved application name. Rithmic commonly permits only one active session per account, so competing software may disconnect an existing session. AMP connections use Rithmic credentials: paper trading typically uses Rithmic Paper Trading and real activity uses the authorized real system.

## Tradovate

Choose Demo (default) or Real, enter Tradovate login plus the API-key CID and secret. Enable real orders separately, preferably with a maximum order size. Tradovate's CME API market data may require a separate entitlement; live trading can also use a compatible CME chart feed. Concurrent data sessions can conflict.

## cTrader

Register an Open API application at `openapi.ctrader.com`, using the callback URL shown by Trading Hub. Set its Client ID and Secret, then authorize a demo or real cTrader account in the browser. A pre-existing access token can also be pasted. Choose the desired account number if the token grants multiple accounts. The token is refreshed and stored in Keychain. For CFDs, footprint volume and delta are **approximations** derived from quotes, not actual exchange trades.

## OANDA

Use a practice or real account, generate an API token in **Manage API Access**, and select the account number (blank uses the first). This connection is **data-only**, with quote-based approximations for footprint and delta.

## Alpaca

Enter an Alpaca API key ID and secret. IEX offers a free single-venue live data selection; SIP is a paid consolidated alternative. Historical US equities data availability depends on entitlement. Trading Hub does **not** route orders to Alpaca.

## Databento

Enter a Databento `db-` API key to access paid CME futures tick history. Testing reports availability and sample costs but does not download data. To obtain data, use **Data → CME futures with Databento**, estimate price first, and explicitly confirm any downloads.

## Interactive Brokers

Run TWS or IB Gateway with API access enabled. Provide host, port, and client ID (common defaults: TWS paper 7497, TWS real 7496, Gateway paper 4002). This integration currently **tests connectivity only**.

## Real account enablement

1. Validate the complete workflow in the simulator or a broker demo/testnet.
2. Switch the provider to its real environment or system.
3. Enable the provider's real-order permission.
4. Set a nonzero maximum order quantity where supported.
5. Save, test, and verify the account is clearly marked **REAL**.

Without explicit authorization, real accounts should remain read-only. Confirm the intended account on **every chart** before placing an order. See [Trading](operar.md#real-money-safeguards).
