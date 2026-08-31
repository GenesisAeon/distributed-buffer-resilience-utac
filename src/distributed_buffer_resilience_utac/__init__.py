"""distributed-buffer-resilience-utac -- distributed hydrological/ecosystem buffer resilience.

GenesisAeon Package 103. Companion to glacier-buffer-utac (P99, the
loss) and glacier-buffer-replacement-utac (P100, technical
replacement): P103 covers the broader "distributed functional
resilience" idea -- a portfolio of reservoirs, groundwater, wetlands
and demand management, each with different response times, rather than
one storage type trying to replace the glacier alone. Deliberately no
UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

Two explicit confidence tiers, kept separate in every module:
- CORE (drought_buffer, storage_portfolio, water_towers,
  ecosystem_services): real, peer-reviewed findings independently
  re-verified 2026-08-14.
- OPTIONAL/SPECULATIVE (gbr): a ratio-style metric this ecosystem
  itself constructed from a source document's own proposed formula,
  not a published metric, always exposed with an explicit warning.
"""

from .constants import (
    ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION,
    CASALLAS_2025_CITATION,
    FARINOTTI_2016_CITATION,
    FARINOTTI_2019_CITATION,
    HUSS_HOCK_2018_CITATION,
    IMMERZEEL_2020_CITATION,
    PACKAGE_ID,
    PRITCHARD_2017_CITATION,
    VAN_TIEL_2026_CITATION,
    WATER_TOWER_DEPENDENT_POPULATION_BILLIONS,
)
from .drought_buffer import (
    SWISS_2022_DROUGHT,
    DroughtBufferObservation,
    buffer_functions_while_eroding,
)
from .ecosystem_services import (
    ECOSYSTEM_SERVICES_CITATION,
    NBS_DESIGN_RULE,
    nbs_effect_is_guaranteed_positive,
)
from .gbr import (
    GBR_NOT_PEER_REVIEWED_WARNING,
    glacier_buffer_replacement_score,
)
from .storage_portfolio import (
    GLOBAL_STORAGE_POTENTIAL,
    STORAGE_PORTFOLIO_NOTE,
    GlobalStoragePotential,
    reservoir_summer_deficit_ceiling_fraction,
    theoretical_vs_realistic_gap_fraction,
)
from .water_towers import (
    is_disproportionate_drought_buffer,
    water_tower_dependent_population_billions,
)

__version__ = "1.0.1"

__all__ = [
    "ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION",
    "CASALLAS_2025_CITATION",
    "ECOSYSTEM_SERVICES_CITATION",
    "FARINOTTI_2016_CITATION",
    "FARINOTTI_2019_CITATION",
    "GBR_NOT_PEER_REVIEWED_WARNING",
    "GLOBAL_STORAGE_POTENTIAL",
    "HUSS_HOCK_2018_CITATION",
    "IMMERZEEL_2020_CITATION",
    "NBS_DESIGN_RULE",
    "PACKAGE_ID",
    "PRITCHARD_2017_CITATION",
    "STORAGE_PORTFOLIO_NOTE",
    "SWISS_2022_DROUGHT",
    "VAN_TIEL_2026_CITATION",
    "WATER_TOWER_DEPENDENT_POPULATION_BILLIONS",
    "DroughtBufferObservation",
    "GlobalStoragePotential",
    "buffer_functions_while_eroding",
    "glacier_buffer_replacement_score",
    "is_disproportionate_drought_buffer",
    "nbs_effect_is_guaranteed_positive",
    "reservoir_summer_deficit_ceiling_fraction",
    "theoretical_vs_realistic_gap_fraction",
    "water_tower_dependent_population_billions",
]
