"""Postglacial ecosystem services: real, but heterogeneous and trade-off-laden.

Core module -- Velasquez Casallas, Khelidj, Moran-Ordonez & Losapio
(2025)'s systematic literature review. The key discipline this module
encodes: Nature-based Solutions are selected by measured local
function, never assumed positive purely from their "natural" label.
"""

from __future__ import annotations

from .constants import CASALLAS_2025_CITATION, CASALLAS_NOTE

NBS_DESIGN_RULE = (
    "Nature-based Solutions are selected by measured local hydrological "
    "function, not by their label. A wetland, a paramo, or reforestation "
    "project is not automatically hydrologically beneficial -- see "
    "CASALLAS_NOTE."
)


def nbs_effect_is_guaranteed_positive() -> bool:
    """Whether a Nature-based Solution's hydrological effect can be assumed positive by its label.

    Always False. Velasquez Casallas et al. (2025)'s systematic review
    found regulating ecosystem services (climate regulation, erosion
    control) can increase after glacier retreat as vegetation
    establishes -- but the effects are spatially/temporally
    heterogeneous with real trade-offs, not a uniform net benefit. Some
    land-use changes framed as 'natural' (e.g. converting paramo to
    pine plantation) measurably REDUCE total and base flow. This
    function exists to make that non-guarantee an explicit, testable
    fact rather than an assumption buried in prose.
    """
    return False


ECOSYSTEM_SERVICES_CITATION = CASALLAS_2025_CITATION
ECOSYSTEM_SERVICES_NOTE = CASALLAS_NOTE
