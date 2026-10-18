[← English documentation](README.md)

# Settings

Use Settings to configure Trading Hub preferences. Settings are persisted locally, generally in `settings.json` under Application Support.

## General

- **Appearance:** choose dark or light mode. Individual chart colors can remain independent of the global theme.
- **Chart time zone:** affects time axes, trade tape, and session display. Select the Mac's local time or a recognized IANA time zone.
- **Alert sounds:** toggles audible notifications for price alerts, large trades, and selected indicators.

## Trading

**Confirm real orders** controls manual order confirmation alongside provider-specific confirmation options. Never turn off confirmation to compensate for an unknown execution or account state. The simulated account shows its configured opening balance.

## Live strategies

Control whether strategies continue when the window closes, whether they resume on application startup, and whether automatic resume is permitted for **real accounts** (off by default). Smart contract selection may choose micro/mini products depending on supported rules.

## Sleep behavior

On macOS, preventing sleep while strategies run can be enabled separately from closed-lid operation. Closed-lid behavior may require administrator authorization and may depend on external power; verify platform-specific behavior rather than assuming it works.

## Keyboard shortcuts

Review shortcut groups for navigation, charts, trading, and other controls. Record conflicts when rebinding. Trading actions are often intentionally unassigned until you choose a safe combination. Escape cancels key recording, and Backspace removes an assignment where supported.

## Data

**Record incoming live market data** stores observed executions for later charts, replay, and backtesting. Buttons open the local data folder, custom-indicator folder, and strategy folder. Understand available disk space and backup needs.

## About

Shows the application version, .NET runtime, and interface technology.

## File locations

Application preferences and data are under `~/Library/Application Support/Trading Hub`. Source indicators and strategies are under `~/Documents/Trading Hub`. Secrets are managed by Keychain rather than the settings file.
