"""Mountain water towers: importance, vulnerability, and disproportionate drought buffering.

Core module -- Immerzeel et al. (2020)'s Water Tower Index and
Pritchard (2017)'s drought-buffer framing, the original source of this
whole package series' central idea.
"""

from __future__ import annotations

from .constants import (
    IMMERZEEL_2020_CITATION,
    IMMERZEEL_NOTE,
    PRITCHARD_2017_CITATION,
    PRITCHARD_NOTE,
    WATER_TOWER_DEPENDENT_POPULATION_BILLIONS,
)


def water_tower_dependent_population_billions() -> float:
    """Global population living in or immediately downstream of mountain water-tower regions."""
    return WATER_TOWER_DEPENDENT_POPULATION_BILLIONS


def is_disproportionate_drought_buffer(
    mean_contribution_pct: float, drought_year_contribution_pct: float
) -> bool:
    """Whether glacier melt contributes disproportionately more during drought than on average.

    Operationalizes Pritchard (2017)'s core finding: glacier melt's
    share of river flow is often small in the long-term mean but much
    larger specifically in low-flow/drought years. True whenever the
    drought-year contribution exceeds the mean contribution.
    """
    if not 0.0 <= mean_contribution_pct <= 100.0:
        raise ValueError(
            f"mean_contribution_pct must be in [0, 100], got {mean_contribution_pct}"
        )
    if not 0.0 <= drought_year_contribution_pct <= 100.0:
        raise ValueError(
            "drought_year_contribution_pct must be in [0, 100], got "
            f"{drought_year_contribution_pct}"
        )
    return drought_year_contribution_pct > mean_contribution_pct


WATER_TOWER_CITATION = IMMERZEEL_2020_CITATION
WATER_TOWER_VULNERABILITY_NOTE = IMMERZEEL_NOTE
DROUGHT_BUFFER_CITATION = PRITCHARD_2017_CITATION
DROUGHT_BUFFER_NOTE = PRITCHARD_NOTE
