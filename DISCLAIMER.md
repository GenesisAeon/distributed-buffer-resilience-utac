# DISCLAIMER — Two Confidence Tiers, No Framework Bridge

**Status: Core = real, independently re-verified science. Optional =
this ecosystem's own discretization of a source document's proposed
formula, not a peer-reviewed metric. NO UTAC/CREP/AFET bridge.**

## Core tier — real, independently re-verified 2026-08-14

Every figure below was checked directly against the paper (DOI lookup
or publisher/press summary) on 2026-08-14.

- **van Tiel, Huss, Zappa, Jonas & Farinotti (2026)**, *HESS* 30,
  23-43, DOI: 10.5194/hess-30-23-2026 — the strongest empirical anchor
  in this package series. 88 glacierized Swiss catchments; 2022 mass
  loss ~6% of remaining volume; glacier melt still substantially
  buffered the 2022 drought's precipitation/snowmelt deficits, while
  absolute summer meltwater volume was already below the comparable
  2003 extreme in roughly two-thirds of catchments. The buffer works
  and its capacity is eroding, simultaneously, already observed.
- **Farinotti, Pistocchi & Huss (2016)**, *ERL* 11(5), 054022, DOI:
  10.1088/1748-9326/11/5/054022 — the ~65% reservoir-strategy ceiling
  on Alpine summer-runoff-CHANGE compensation, reused from P100 with
  the same scoping discipline: a specific regional scenario-bound
  estimate, not a universal replacement constant. Farinotti et al.
  explicitly state reservoirs cannot compensate the annual
  non-renewable runoff share permanently lost as glacier ice
  disappears.
- **Farinotti, Round, Huss, Compagno & Zekollari (2019)**, *Nature*
  575, 341-344, DOI: 10.1038/s41586-019-1740-z — global theoretical
  ice-free-basin storage potential (875±260 km³ across ~185,000
  glaciers analyzed), of which only ~40% (355 km³) was judged
  potentially suitable after a first-pass technical/ecological/
  economic screen. The paper itself stresses the theoretical character
  of the 875 km³ figure.
- **Huss & Hock (2018)**, *Nature Climate Change* 8, 135-140, DOI:
  10.1038/s41558-017-0049-x — "peak water" (reused from P99).
- **Pritchard (2017)**, *Nature* 545, 169-174, DOI:
  10.1038/nature22062 — the origin of the "glaciers as a regionally
  important drought buffer" framing this entire package series builds
  on.
- **Immerzeel, Lutz, Andrade et al. (2020)**, *Nature* 577, 364-369,
  DOI: 10.1038/s41586-019-1822-y — the Water Tower Index: 1.9 billion
  people dependent globally; some of the most hydrologically important
  water towers (Indus, Amu Darya, Tarim) are simultaneously among the
  most vulnerable.
- **Velasquez Casallas, Khelidj, Moran-Ordonez & Losapio (2025)**,
  *Ecosystem Services* 73, 101730, DOI: 10.1016/j.ecoser.2025.101730 —
  a systematic literature review: postglacial regulating ecosystem
  services (climate regulation, erosion control) can increase, but
  heterogeneously, with real trade-offs — not a uniform net benefit.

## Optional tier — this ecosystem's own construction, flagged

- **`gbr.py`'s Glacier Buffer Replacement (GBR) score** is **not a
  peer-reviewed metric**. It is a discretized implementation of a
  formula proposed in `P102.md` (Kimi's own synthesis, itself building
  on this package's real drought/streamflow evidence) — the scoring
  formula carries no primary citation. This mirrors
  `glacier-buffer-replacement-utac` (P100)'s Resilience Replacement
  Factor precedent: every function in `gbr.py` is exported alongside
  `GBR_NOT_PEER_REVIEWED_WARNING`.

## What this is NOT

- **Not a claim that ecosystem restoration or storage portfolios fully
  replace lost glacier hydrology.** `theoretical_vs_realistic_gap_fraction()`
  and `FARINOTTI_2016_SCOPE_NOTE` make the same physical ceiling
  explicit that P100's `mass_balance` module encodes for reservoirs
  alone: this package broadens the portfolio, it does not remove the
  underlying mass-balance limit.
- **`nbs_effect_is_guaranteed_positive()` always returns `False`** —
  intentionally. Nature-based Solutions are real and often valuable,
  but their hydrological effect must be measured locally, never
  assumed from the "natural" label.
- **No UTAC/CREP/AFET bridge.** This is a real, standalone hydrology
  and ecosystem-science topic; the cited papers already provide the
  relevant quantitative structure without this ecosystem's
  cross-domain vocabulary.

## References

- van Tiel, M., Huss, M., Zappa, M., Jonas, T., Farinotti, D. (2026).
  *HESS*, 30, 23-43. DOI: 10.5194/hess-30-23-2026.
- Farinotti, D., Pistocchi, A., Huss, M. (2016). *ERL*, 11(5), 054022.
  DOI: 10.1088/1748-9326/11/5/054022.
- Farinotti, D., Round, V., Huss, M., Compagno, L., Zekollari, H.
  (2019). *Nature*, 575, 341-344. DOI: 10.1038/s41586-019-1740-z.
- Huss, M., Hock, R. (2018). *Nature Climate Change*, 8, 135-140. DOI:
  10.1038/s41558-017-0049-x.
- Pritchard, H.D. (2017). *Nature*, 545, 169-174. DOI:
  10.1038/nature22062.
- Immerzeel, W.W., Lutz, A.F., Andrade, M. et al. (2020). *Nature*,
  577, 364-369. DOI: 10.1038/s41586-019-1822-y.
- Velasquez Casallas, L.M., Khelidj, N., Moran-Ordonez, A., Losapio, G.
  (2025). *Ecosystem Services*, 73, 101730. DOI:
  10.1016/j.ecoser.2025.101730.

All verified directly (2026-08-14) via WebSearch against the
publisher/journal record for each paper. Originating dialogue:
`P 102.txt` (Johann + Kimi) and `P102.md` (Kimi's own deep-research
audit, which proposed splitting P102 into a paraglacial-hazard package
[P102, see `paraglacial-hazard-utac`] and this hydrological/ecosystem
package [P103] rather than one monolithic three-pillar package —
independently spot-checked before building either).
