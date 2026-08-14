"""The empirical anchor: glacier drought buffering is real but eroding.

Core module -- van Tiel, Huss, Zappa, Jonas & Farinotti (2026)'s Swiss
2022-drought analysis, the strongest current empirical evidence for
this whole package series' central claim: the natural buffer still
functions during extreme events, even as its physical capacity shrinks.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    VAN_TIEL_2022_MASS_LOSS_PCT,
    VAN_TIEL_2026_CITATION,
    VAN_TIEL_CATCHMENT_COUNT,
    VAN_TIEL_NOTE,
)


@dataclass(frozen=True)
class DroughtBufferObservation:
    """A real, dated observation of glacier drought-buffering under extreme conditions."""

    catchment_count: int
    mass_loss_pct: float
    note: str
    citation: str


SWISS_2022_DROUGHT = DroughtBufferObservation(
    catchment_count=VAN_TIEL_CATCHMENT_COUNT,
    mass_loss_pct=VAN_TIEL_2022_MASS_LOSS_PCT,
    note=VAN_TIEL_NOTE,
    citation=VAN_TIEL_2026_CITATION,
)


def buffer_functions_while_eroding() -> bool:
    """The core van Tiel et al. (2026) finding: both things are true at once.

    Always True. During the extreme 2022 Swiss drought, glacier melt
    still substantially buffered precipitation/snowmelt deficits AND
    the absolute meltwater volume was already below the comparable 2003
    extreme in roughly two-thirds of studied catchments. A buffer that
    still 'works' in the present is not evidence its capacity isn't
    shrinking -- this is the empirical basis for treating resilience
    loss as something that can precede visible system failure (see
    P102.md's Adaptive Option Capacity discussion, not implemented here
    as code -- too undefined for that, see DISCLAIMER.md).
    """
    return True
