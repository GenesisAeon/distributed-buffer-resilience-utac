"""Storage portfolio: technical reservoirs plus complementary response-time buffers.

Core module -- Farinotti et al. (2016, 2019) for the quantified
reservoir/storage figures. The response-time categorization is a
qualitative, widely-used framing in mountain hydrology (not itself tied
to one paper) illustrating why P102.md argues for a PORTFOLIO of
buffers rather than a single largest-volume one -- see
STORAGE_PORTFOLIO_NOTE.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION,
    FARINOTTI_2016_CITATION,
    FARINOTTI_2016_SCOPE_NOTE,
    FARINOTTI_2019_CITATION,
    FARINOTTI_2019_NOTE,
    GLOBAL_THEORETICAL_HYDROPOWER_POTENTIAL_TWH_PER_YR,
    GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3,
    GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3_UNCERTAINTY,
    REALISTIC_HYDROPOWER_POTENTIAL_TWH_PER_YR,
    REALISTIC_STORAGE_FRACTION_OF_THEORETICAL,
    REALISTIC_STORAGE_POTENTIAL_KM3,
)

STORAGE_PORTFOLIO_NOTE = (
    "A moor, a floodplain, an aquifer and a reservoir can all 'store "
    "water', but their impulse responses differ fundamentally: snow "
    "(seasonal), reservoirs (managed, fast release), soil moisture "
    "(days-weeks), wetlands (weeks-months), groundwater (months-years). "
    "Two systems with identical total storage volume can have very "
    "different drought resilience because accessibility, retention "
    "time, evaporation exposure, spatial position and release dynamics "
    "differ. This is a widely-used qualitative framing in mountain "
    "hydrology, not a single-paper citation -- see P99/P100 for the "
    "component-specific quantified figures (sedimentation, MAR "
    "retention time, floating-solar evaporation mitigation, etc.)."
)


def reservoir_summer_deficit_ceiling_fraction(
    with_citation: bool = False,
) -> float | tuple[float, str]:
    """The Farinotti et al. (2016) reservoir-strategy ceiling on Alpine summer-deficit compensation.

    A specific, regional, scenario-bound estimate (European Alps, to
    2100) -- NOT a universal replacement constant. See
    FARINOTTI_2016_SCOPE_NOTE.
    """
    if with_citation:
        return ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION, FARINOTTI_2016_CITATION
    return ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION


@dataclass(frozen=True)
class GlobalStoragePotential:
    """Farinotti et al. (2019)'s global theoretical vs. realistic storage potential."""

    theoretical_km3: float
    theoretical_km3_uncertainty: float
    theoretical_hydropower_twh_per_yr: float
    realistic_fraction: float
    realistic_km3: float
    realistic_hydropower_twh_per_yr: float
    citation: str


GLOBAL_STORAGE_POTENTIAL = GlobalStoragePotential(
    theoretical_km3=GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3,
    theoretical_km3_uncertainty=GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3_UNCERTAINTY,
    theoretical_hydropower_twh_per_yr=GLOBAL_THEORETICAL_HYDROPOWER_POTENTIAL_TWH_PER_YR,
    realistic_fraction=REALISTIC_STORAGE_FRACTION_OF_THEORETICAL,
    realistic_km3=REALISTIC_STORAGE_POTENTIAL_KM3,
    realistic_hydropower_twh_per_yr=REALISTIC_HYDROPOWER_POTENTIAL_TWH_PER_YR,
    citation=FARINOTTI_2019_CITATION,
)


def theoretical_vs_realistic_gap_fraction() -> float:
    """Fraction of the theoretical global storage potential judged NOT realistically suitable.

    1 - realistic_fraction, i.e. how much of Farinotti et al. (2019)'s
    theoretical 875 km3 figure falls away after a first-pass technical/
    ecological/economic suitability screen. See FARINOTTI_2019_NOTE.
    """
    return 1.0 - GLOBAL_STORAGE_POTENTIAL.realistic_fraction


FARINOTTI_2016_NOTE = FARINOTTI_2016_SCOPE_NOTE
FARINOTTI_2019_SCOPE_NOTE = FARINOTTI_2019_NOTE
