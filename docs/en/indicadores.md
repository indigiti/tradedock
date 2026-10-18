[← English documentation](README.md)

# Indicators

Trading Hub provides native indicators and supports custom C# implementations.

## Included indicators

Technical studies include simple and exponential moving averages, VWAP and its deviation bands, Bollinger Bands, RSI, MACD, volume, delta, cumulative delta (CVD), session volume profile, and large trades. Indicator display may use the main price chart or a dedicated panel.

## Adding and configuring indicators

Open the Indicators window on a chart, select a study from the library, add it, and edit its settings. Use the show/hide control, move between price and independent panels where supported, and remove studies as needed. Templates can preserve individual indicator parameters and appearance.

## Your own C# indicators

Place C# indicator files in `~/Documents/Trading Hub/Indicadores`. The application monitors and compiles these with Roslyn; edits can be recompiled while using the platform. Open the indicator editor from the Code menu. Compilation errors should be reviewed before attaching an indicator to real-time data.

Custom indicators should use the provided SDK conventions for access to candles, price series, volume series, parameters, calculation lifecycle, and drawings. Review the codebase examples before adopting external indicator APIs.

## ATAS compatibility

The repository provides an adaptation script for indicators from the public ATAS indicator repository. Source licensing varies; indicators are not included automatically.

```bash
git clone https://github.com/AtasPlatform/Indicators.git third_party/ATAS-Indicators
python3 tools/port_atas.py
./build-app.sh --install
```

The compatibility adapter adjusts namespaces and a small number of compilation details. It does not grant the right to redistribute someone else's source. If an imported indicator depends on another indicator or DLL, supply that dependency separately and check its licensing terms.

## Validation checklist

Compare output to known indicator results on fixed historical datasets, verify correct behavior on live forming candles, test a variety of timeframes, and confirm no look-ahead bias or state contamination between symbols.
