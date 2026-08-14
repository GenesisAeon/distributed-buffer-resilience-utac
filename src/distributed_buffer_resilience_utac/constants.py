"""Verified constants for distributed hydrological/ecosystem buffer resilience.

Companion to glacier-buffer-utac (P99, the natural loss) and
glacier-buffer-replacement-utac (P100, technical replacement). P103
covers the broader "distributed functional resilience" idea from
P102.md: instead of one storage type replacing the glacier, a portfolio
of reservoirs, groundwater, wetlands and demand management, each with
different response times, is what actually buffers a deglacierizing
catchment.

Two explicit confidence tiers, kept separate throughout this package:
- CORE: real, peer-reviewed findings independently re-verified via
  direct paper/DOI lookup on 2026-08-14.
- OPTIONAL/SPECULATIVE (see gbr.py): a ratio-style metric this
  ecosystem itself constructed (following P102.md's own proposal),
  not a published, peer-reviewed formula -- exposed with an explicit
  warning constant, same pattern as P100's RRF.
"""

PACKAGE_ID = 103

# =====================================================================
# CORE -- independently re-verified 2026-08-14
# =====================================================================

# --- van Tiel, Huss, Zappa, Jonas & Farinotti 2026: the empirical anchor ---

VAN_TIEL_2026_CITATION = (
    "van Tiel, M., Huss, M., Zappa, M., Jonas, T., Farinotti, D. "
    "(2026). Swiss glacier mass loss during the 2022 drought: "
    "persistent streamflow contributions amid declining melt water "
    "volumes. Hydrology and Earth System Sciences, 30, 23-43. "
    "DOI: 10.5194/hess-30-23-2026"
)
VAN_TIEL_2026_DOI = "10.5194/hess-30-23-2026"

# Number of glacierized Swiss catchments analyzed
VAN_TIEL_CATCHMENT_COUNT = 88
# Swiss glacier mass lost during 2022 alone, percent of remaining volume
VAN_TIEL_2022_MASS_LOSS_PCT = 6.0

VAN_TIEL_NOTE = (
    "This is currently the strongest single empirical anchor for the "
    "whole P99-P103 series: during the extreme, hot, dry summer of "
    "2022, glacier melt across 88 Swiss catchments STILL substantially "
    "buffered precipitation/snowmelt deficits -- yet in roughly "
    "two-thirds of the studied catchments, the absolute summer "
    "meltwater volume was already LOWER than in the comparably extreme "
    "2003 summer, because shrinking glacier area increasingly "
    "outweighs higher specific melt rates. The buffer still works, but "
    "its physical capacity is measurably eroding -- not a hypothetical "
    "future transition, an already-observed one."
)

# --- Farinotti, Pistocchi & Huss 2016: reservoir ceiling (reused from P100) ---

FARINOTTI_2016_CITATION = (
    "Farinotti, D., Pistocchi, A., Huss, M. (2016). From dwindling ice "
    "to headwater lakes: could dams replace glaciers in the European "
    "Alps? Environmental Research Letters, 11(5), 054022. "
    "DOI: 10.1088/1748-9326/11/5/054022"
)
FARINOTTI_2016_DOI = "10.1088/1748-9326/11/5/054022"

# Ceiling on the fraction of the projected end-of-century Alpine
# summer-runoff CHANGE (not total hydrological loss) a reservoir
# strategy could offset -- a specific, regional, scenario-bound
# estimate, NOT a universal replacement constant. See P100's
# mass_balance module for the same figure applied to reservoirs alone;
# here it anchors the "technical storage" layer of the wider portfolio.
ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION = 0.65

FARINOTTI_2016_SCOPE_NOTE = (
    "Farinotti et al. (2016) found NO general physical upper bound of "
    "65% for technical glacier replacement. They estimated that, for a "
    "specific European Alps scenario to 2100, reservoir management "
    "could offset up to ~65% of the EXPECTED CHANGE in summer runoff "
    "from presently glacierized areas -- and explicitly state that "
    "reservoirs cannot compensate the annual non-renewable runoff share "
    "lost as glacier ice permanently disappears. Treat 65% as a "
    "modeled, regional, scenario-bound ceiling, never as a portable "
    "'universal replacement fraction'."
)

# --- Farinotti et al. 2019: global storage potential in ice-free basins ---

FARINOTTI_2019_CITATION = (
    "Farinotti, D., Round, V., Huss, M., Compagno, L., Zekollari, H. "
    "(2019). Large hydropower and water-storage potential in future "
    "glacier-free basins. Nature, 575, 341-344. "
    "DOI: 10.1038/s41586-019-1740-z"
)
FARINOTTI_2019_DOI = "10.1038/s41586-019-1740-z"

# Global theoretical storage potential in future ice-free glacier
# basins, km^3 (based on ~185,000 glaciers analyzed)
GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3 = 875.0
GLOBAL_THEORETICAL_STORAGE_POTENTIAL_KM3_UNCERTAINTY = 260.0
GLOBAL_THEORETICAL_HYDROPOWER_POTENTIAL_TWH_PER_YR = 1350.0

# After a first technical/ecological/economic suitability screen, the
# fraction of the theoretical potential judged "potentially" realistic
REALISTIC_STORAGE_FRACTION_OF_THEORETICAL = 0.40
REALISTIC_STORAGE_POTENTIAL_KM3 = 355.0
REALISTIC_HYDROPOWER_POTENTIAL_TWH_PER_YR = 533.0

FARINOTTI_2019_NOTE = (
    "875 +/- 260 km3 is a global THEORETICAL maximum across ~185,000 "
    "glaciers; only ~40% (355 km3) passed a first-pass technical, "
    "ecological and economic suitability screen. The paper itself "
    "stresses this remains theoretical and requires site-specific "
    "assessment before any real project -- do not read 875 km3 as "
    "'available' storage."
)

# --- Huss & Hock 2018: peak water (reused from P99) ---

HUSS_HOCK_2018_CITATION = (
    "Huss, M., Hock, R. (2018). Global-scale hydrological response to "
    "future glacier mass loss. Nature Climate Change, 8, 135-140. "
    "DOI: 10.1038/s41558-017-0049-x"
)
HUSS_HOCK_2018_DOI = "10.1038/s41558-017-0049-x"

# --- Pritchard 2017: glaciers as a regional drought buffer ---

PRITCHARD_2017_CITATION = (
    "Pritchard, H.D. (2017). Asia's glaciers are a regionally important "
    "buffer against drought. Nature, 545, 169-174. "
    "DOI: 10.1038/nature22062"
)
PRITCHARD_2017_DOI = "10.1038/nature22062"

PRITCHARD_NOTE = (
    "Pritchard (2017) is the explicit origin of the 'glaciers as "
    "drought buffer' framing this whole package series builds on: "
    "glacier meltwater contribution to river flow is disproportionately "
    "important precisely during low-flow/drought years in High Mountain "
    "Asia, even in basins where glacier melt is a small share of the "
    "long-term mean flow."
)

# --- Immerzeel et al. 2020: Water Tower Index ---

IMMERZEEL_2020_CITATION = (
    "Immerzeel, W.W., Lutz, A.F., Andrade, M. et al. (2020). "
    "Importance and vulnerability of the world's water towers. Nature, "
    "577, 364-369. DOI: 10.1038/s41586-019-1822-y"
)
IMMERZEEL_2020_DOI = "10.1038/s41586-019-1822-y"

# Global population living in or immediately downstream of mountain
# water-tower regions, billions
WATER_TOWER_DEPENDENT_POPULATION_BILLIONS = 1.9

IMMERZEEL_NOTE = (
    "The Water Tower Index ranks mountain water systems not just by "
    "hydrological importance but also by water stress, governance "
    "quality, hydropolitical tension, and climatic/socioeconomic "
    "change -- some of the world's most important water towers "
    "(Indus, Amu Darya, Tarim) are simultaneously among the most "
    "vulnerable, precisely because high dependence coincides with weak "
    "governance capacity."
)

# --- Velasquez Casallas, Khelidj, Moran-Ordonez & Losapio 2025: ecosystem services ---

CASALLAS_2025_CITATION = (
    "Velasquez Casallas, L.M., Khelidj, N., Moran-Ordonez, A., "
    "Losapio, G. (2025). Global impacts of glacier retreat on "
    "ecosystem services provided by soil and vegetation in mountain "
    "regions: A literature review. Ecosystem Services, 73, 101730. "
    "DOI: 10.1016/j.ecoser.2025.101730"
)
CASALLAS_2025_DOI = "10.1016/j.ecoser.2025.101730"

CASALLAS_NOTE = (
    "This systematic review found that regulating ecosystem services "
    "(e.g. climate regulation, erosion control) can INCREASE in "
    "postglacial landscapes as vegetation establishes -- but the "
    "effects are spatially and temporally heterogeneous, with real "
    "trade-offs against other services, not a uniform net benefit. "
    "Nature-based solutions should be selected by measured local "
    "function, never assumed positive purely from their 'natural' "
    "label -- see ecosystem_services.py."
)
