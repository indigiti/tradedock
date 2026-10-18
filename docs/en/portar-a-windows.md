[← English documentation](README.md)

# Port Trading Hub to Windows

Trading Hub currently targets Apple Silicon macOS, but Avalonia/.NET 10 are cross-platform. A Windows release is a **porting project**, not simply an installer switch.

## Prepare

Use Windows 10 or 11 (64-bit), Git, .NET 10 SDK, and optionally Claude Code. Read `README.md`, `CLAUDE.md`, and the upstream Spanish [Windows inventory](../../PORTAR_A_WINDOWS.md).

## macOS-specific features to replace

| macOS dependency | Windows equivalent |
|---|---|
| Keychain secrets | Credential Manager (`CredWrite`/`CredRead`/`CredDelete`) or DPAPI |
| Menu-bar agent | System tray and native window activation |
| Keep-awake behavior | `SetThreadExecutionState` and Windows power-state checks |
| `afplay` notifications | Windows-compatible audio |
| macOS titlebar/traffic lights | Windows titlebar controls |
| Command shortcuts | Ctrl equivalents, with a shared shortcut abstraction |
| Finder/open shell behavior | Windows shell and `UseShellExecute` |
| Claude CLI path lookup | `claude.exe`/`claude.cmd`, PATH, user install locations |

## Suggested phased implementation

1. Make core startup, fonts, data paths, and project compilation work on Windows.
2. Introduce a secrets interface and a Windows implementation. Keep macOS Keychain unchanged.
3. Port tray, sleep prevention, links, sounds, and Claude Code discovery.
4. Adapt keyboard shortcuts, title bar, labels, and app-specific interactions.
5. Publish self-contained `win-x64` (and optionally `win-arm64`) builds, with packaging metadata and icon.
6. Run unit tests, headless UI scenes, and manual simulated-account smoke tests on Windows and macOS.

Prefer isolated platform services such as `ISecretStore`, `ISleepGuard`, `IShell`, or `ISound` rather than duplicating entire views. Do not write credentials to unencrypted text files.

## Validation gates

Run after each phase:

```bash
dotnet build TradingHub.slnx
dotnet test tests/TradingHub.Tests
```

Then inspect data import, chart histories, drawing persistence, simulated order entry/exit, broker reconnection, and localization behavior. Do not turn on real orders while porting or testing.

## Windows-specific limitations

Some macOS features, such as intentionally operating with a closed laptop lid, may not have identical Windows behavior. Hide unavailable options or explain their limitations clearly. Show actual error messages and preserve existing macOS functionality.

For the complete original implementation inventory, consult the [Spanish Windows guide](../../PORTAR_A_WINDOWS.md).
