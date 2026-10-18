# TradeDock — English localization validation dashboard

**Last reviewed:** 2026-10-18  
**Working branch:** `translation/english-documentation-ui`  
**Change request:** [Draft PR #1](https://github.com/indigiti/tradedock/pull/1)  
**Release gate:** **BLOCKED — do not merge until remaining checks are verified.**

## Goals and scope

Deliver an understandable English trading application and English project documentation while preserving the existing macOS trading behavior, order safety, brokers, market data, indicators, backtesting, and stored user files.

## Evidence and current state

| Workstream | State | Evidence | Remaining acceptance criteria |
|---|---|---|---|
| English top-level README | Complete | `README.md`; `README.es.md` retained | Review link targets and content accuracy |
| English documentation access | Available, condensed | 17 English guide files in `docs/en/`, including index | Full section-by-section translation parity against each original Spanish guide |
| Source UI labels | Partial | 20 application C# files changed, 355-item glossary in `tools/english-ui-glossary.json` | Inspect all remaining static, dynamic, dialog, and indicator strings |
| Trading algorithm changes | None intended | Existing changes are quoted-label substitutions | Confirm with `tools/check_english_translation.py` on every PR run |
| .NET 10 macOS build | Passed on initial CI run | [GitHub Actions](https://github.com/indigiti/tradedock/actions/runs/39139263418) | Revalidate after subsequent changes |
| Existing unit/regression suite | Passed on initial CI run | [GitHub Actions](https://github.com/indigiti/tradedock/actions/runs/39139263418) | Revalidate after subsequent changes |
| English documentation links | Pending automated gate | `tools/check_english_translation.py` | All relative links resolve |
| UI string-only diff guard | Pending automated gate | Compares translated source to `origin/main` using approved exact-literal translations | No unexplained source edits |
| Desktop visual and UX review | Not run | No reviewed screenshots | Test navigation, clipping, hotkeys, icon labels, responsive layouts, dialogs |
| Live/paper broker regression | Not run | No authorized live account test | Test reconnections and error paths with safe fixtures; never expose credentials |
| Release readiness | **Blocked** | Draft PR is intentionally unmerged | All high-risk unresolved issues closed with evidence |

## Risks and blockers

1. Numerous Spanish labels remain in interpolated status text and secondary dialogs. A successful compilation is not a full localization check.
2. The generated indicator localization file `Strings.g.cs` has mixed Spanish and English values. Do not edit generated output directly; address its generation or localization source.
3. The detailed English guides are curated condensations. The complete Spanish docs remain the source of record until line-by-line parity is reviewed.
4. English string length can cause truncation in chart toolbars, narrow windows, and confirmation dialogs.
5. Real-money confirmation, disable/stop, close-position, and broker reconnection messages require bilingual accuracy review before the interface is considered ready.
6. CI covers existing build and test targets, not a complete live-broker or GUI integration simulation.

## Regression requirements

- **Code integrity:** No changes to order routing, broker authentication, account permissions, live feed, data storage, replay, indicator math, or backtest behavior except explicitly reviewed localization substitutions.
- **Risk:** Simulation remains default; real execution remains opt-in; order limits and confirmations remain unchanged.
- **Data:** Historical tick/candle reading, chart state persistence, and import/export formats remain compatible.
- **UX:** Confirm safe English prompts, navigation, shortcuts, readable columns, tooltips, and window layouts.
- **Testing:** The PR must show green automated checks and reviewed manual UI evidence before merge.

## Release decision

**Not ready for merge.** Initial build/tests passed; source-only and documentation validation will run in CI, but complete localization and visual review are unfinished. Keep PR #1 in draft.

## Reference links

- [PR #1](https://github.com/indigiti/tradedock/pull/1)
- [CI workflow](../../.github/workflows/english-translation-validation.yml)
- [UI glossary](../../tools/english-ui-glossary.json)
- [Validation script](../../tools/check_english_translation.py)
- [Original Spanish README](../../README.es.md)
