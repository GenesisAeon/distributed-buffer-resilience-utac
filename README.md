# distributed-buffer-resilience-utac

GenesisAeon Package 103 — distributed hydrological/ecosystem buffer
resilience for deglacierizing catchments. Companion to
[glacier-buffer-utac](https://github.com/GenesisAeon/glacier-buffer-utac)
(P99, the loss) and
[glacier-buffer-replacement-utac](https://github.com/GenesisAeon/glacier-buffer-replacement-utac)
(P100, technical replacement). **Deliberately has no UTAC/CREP/AFET
bridge** — see [DISCLAIMER.md](DISCLAIMER.md).

## The core idea

A single storage type can't replace a glacier. What actually buffers a
deglacierizing catchment is a **portfolio** of reservoirs, groundwater,
wetlands, snow, and demand management, each with a different response
time — not one component sized to do the whole job.

## Two explicit confidence tiers

- **Core** (`drought_buffer`, `storage_portfolio`, `water_towers`,
  `ecosystem_services`): real, peer-reviewed findings independently
  re-verified 2026-08-14.
- **Optional / speculative** (`gbr`): a ratio-style score this
  ecosystem constructed from a source document's own proposed formula
  — not a published metric. Always exposed with
  `GBR_NOT_PEER_REVIEWED_WARNING`.

## What's real here (core)

- **van Tiel et al. (2026, *HESS*)** — the strongest empirical anchor
  in the whole P99–P103 series: during the extreme 2022 Swiss drought,
  glacier melt across 88 catchments still substantially buffered
  precipitation/snowmelt deficits — yet absolute summer meltwater
  volume was already lower than 2003 in roughly two-thirds of studied
  catchments. The buffer works AND its capacity is eroding, at the
  same time, already observed, not projected.
- **Farinotti et al. (2016, *ERL*)** — the ~65% Alpine reservoir
  summer-deficit ceiling, correctly scoped as a specific, regional,
  scenario-bound estimate (not a universal constant — see
  `FARINOTTI_2016_SCOPE_NOTE`).
- **Farinotti et al. (2019, *Nature*)** — global theoretical
  ice-free-basin storage potential (875±260 km³ across ~185,000
  glaciers), with only ~40% (355 km³) judged realistically suitable
  after a first-pass screen.
- **Pritchard (2017, *Nature*)** and **Immerzeel et al. (2020,
  *Nature*)** — glaciers as a disproportionate drought buffer, and the
  Water Tower Index ranking mountain water systems by importance AND
  vulnerability (1.9 billion people dependent globally).
- **Velasquez Casallas et al. (2025, *Ecosystem Services*)** — a
  systematic review finding postglacial ecosystem services can
  increase, but heterogeneously, with real trade-offs — never assume a
  Nature-based Solution is hydrologically positive purely from its
  label. `nbs_effect_is_guaranteed_positive()` always returns `False`.

## Quickstart

```bash
pip install distributed-buffer-resilience-utac
```

```python
from distributed_buffer_resilience_utac import (
    SWISS_2022_DROUGHT,
    buffer_functions_while_eroding,
    reservoir_summer_deficit_ceiling_fraction,
    GLOBAL_STORAGE_POTENTIAL,
    is_disproportionate_drought_buffer,
    nbs_effect_is_guaranteed_positive,
    GBR_NOT_PEER_REVIEWED_WARNING,
    glacier_buffer_replacement_score,
)

print(SWISS_2022_DROUGHT.catchment_count)          # 88
print(buffer_functions_while_eroding())             # True
print(reservoir_summer_deficit_ceiling_fraction())  # 0.65
print(GLOBAL_STORAGE_POTENTIAL.realistic_km3)       # 355.0
print(is_disproportionate_drought_buffer(10.0, 40.0))  # True
print(nbs_effect_is_guaranteed_positive())          # False

print(GBR_NOT_PEER_REVIEWED_WARNING)
score = glacier_buffer_replacement_score(
    deficit_without_adaptation=[10.0, 10.0],
    flow_gain_from_adaptation=[5.0, 0.0],
)
print(score)  # 0.25
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
