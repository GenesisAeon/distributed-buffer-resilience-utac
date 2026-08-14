"""Tests for distributed-buffer-resilience-utac."""

import pytest

from distributed_buffer_resilience_utac import (
    ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION,
    GBR_NOT_PEER_REVIEWED_WARNING,
    GLOBAL_STORAGE_POTENTIAL,
    NBS_DESIGN_RULE,
    PACKAGE_ID,
    SWISS_2022_DROUGHT,
    WATER_TOWER_DEPENDENT_POPULATION_BILLIONS,
    __version__,
    buffer_functions_while_eroding,
    glacier_buffer_replacement_score,
    is_disproportionate_drought_buffer,
    nbs_effect_is_guaranteed_positive,
    reservoir_summer_deficit_ceiling_fraction,
    theoretical_vs_realistic_gap_fraction,
    water_tower_dependent_population_billions,
)


def test_version():
    assert __version__ == "1.0.0"


def test_package_id():
    assert PACKAGE_ID == 103


# --- drought_buffer.py (core) ------------------------------------------------


def test_swiss_2022_drought_values():
    assert SWISS_2022_DROUGHT.catchment_count == 88
    assert SWISS_2022_DROUGHT.mass_loss_pct == pytest.approx(6.0)
    assert SWISS_2022_DROUGHT.citation


def test_buffer_functions_while_eroding():
    assert buffer_functions_while_eroding() is True


# --- storage_portfolio.py (core) ---------------------------------------------


def test_reservoir_summer_deficit_ceiling_fraction():
    assert reservoir_summer_deficit_ceiling_fraction() == pytest.approx(0.65)
    assert reservoir_summer_deficit_ceiling_fraction() == pytest.approx(
        ALPINE_RESERVOIR_SUMMER_DEFICIT_CEILING_FRACTION
    )


def test_reservoir_summer_deficit_ceiling_fraction_with_citation():
    value, citation = reservoir_summer_deficit_ceiling_fraction(with_citation=True)
    assert value == pytest.approx(0.65)
    assert "Farinotti" in citation


def test_global_storage_potential_values():
    assert GLOBAL_STORAGE_POTENTIAL.theoretical_km3 == pytest.approx(875.0)
    assert GLOBAL_STORAGE_POTENTIAL.theoretical_km3_uncertainty == pytest.approx(260.0)
    assert GLOBAL_STORAGE_POTENTIAL.realistic_km3 == pytest.approx(355.0)
    assert GLOBAL_STORAGE_POTENTIAL.realistic_fraction == pytest.approx(0.40)
    assert GLOBAL_STORAGE_POTENTIAL.citation


def test_theoretical_vs_realistic_gap_fraction():
    assert theoretical_vs_realistic_gap_fraction() == pytest.approx(0.60)


# --- water_towers.py (core) --------------------------------------------------


def test_water_tower_dependent_population_billions():
    assert water_tower_dependent_population_billions() == pytest.approx(1.9)
    assert WATER_TOWER_DEPENDENT_POPULATION_BILLIONS == pytest.approx(1.9)


def test_is_disproportionate_drought_buffer_true():
    assert is_disproportionate_drought_buffer(10.0, 40.0) is True


def test_is_disproportionate_drought_buffer_false():
    assert is_disproportionate_drought_buffer(40.0, 10.0) is False


def test_is_disproportionate_drought_buffer_rejects_out_of_range():
    with pytest.raises(ValueError, match=r"must be in \[0, 100\]"):
        is_disproportionate_drought_buffer(-1.0, 50.0)
    with pytest.raises(ValueError, match=r"must be in \[0, 100\]"):
        is_disproportionate_drought_buffer(50.0, 101.0)


# --- ecosystem_services.py (core) --------------------------------------------


def test_nbs_effect_is_guaranteed_positive_always_false():
    assert nbs_effect_is_guaranteed_positive() is False


def test_nbs_design_rule_mentions_function_not_label():
    assert "function" in NBS_DESIGN_RULE.lower()
    assert "label" in NBS_DESIGN_RULE.lower()


# --- gbr.py (speculative) -----------------------------------------------------


def test_gbr_warning_present_and_explicit():
    assert "NOT" in GBR_NOT_PEER_REVIEWED_WARNING
    assert "peer-reviewed" in GBR_NOT_PEER_REVIEWED_WARNING.lower()


def test_glacier_buffer_replacement_score_full_compensation():
    score = glacier_buffer_replacement_score(
        deficit_without_adaptation=[10.0, 10.0], flow_gain_from_adaptation=[10.0, 10.0]
    )
    assert score == pytest.approx(1.0)


def test_glacier_buffer_replacement_score_no_compensation():
    score = glacier_buffer_replacement_score(
        deficit_without_adaptation=[10.0, 10.0], flow_gain_from_adaptation=[0.0, 0.0]
    )
    assert score == pytest.approx(0.0)


def test_glacier_buffer_replacement_score_partial_compensation():
    score = glacier_buffer_replacement_score(
        deficit_without_adaptation=[10.0, 10.0], flow_gain_from_adaptation=[5.0, 0.0]
    )
    assert score == pytest.approx(0.25)


def test_glacier_buffer_replacement_score_overshoot_capped_per_timestep():
    # Gain of 20 against a deficit of only 10 in that timestep is capped at 10
    score = glacier_buffer_replacement_score(
        deficit_without_adaptation=[10.0, 10.0], flow_gain_from_adaptation=[20.0, 0.0]
    )
    assert score == pytest.approx(0.5)


def test_glacier_buffer_replacement_score_can_go_negative():
    score = glacier_buffer_replacement_score(
        deficit_without_adaptation=[10.0], flow_gain_from_adaptation=[-5.0]
    )
    assert score == pytest.approx(-0.5)


def test_glacier_buffer_replacement_score_rejects_mismatched_lengths():
    with pytest.raises(ValueError, match="equal length"):
        glacier_buffer_replacement_score([10.0, 10.0], [5.0])


def test_glacier_buffer_replacement_score_rejects_empty_input():
    with pytest.raises(ValueError, match="non-empty"):
        glacier_buffer_replacement_score([], [])


def test_glacier_buffer_replacement_score_rejects_negative_deficit():
    with pytest.raises(ValueError, match="non-negative"):
        glacier_buffer_replacement_score([-1.0], [1.0])


def test_glacier_buffer_replacement_score_rejects_zero_total_deficit():
    with pytest.raises(ValueError, match="zero"):
        glacier_buffer_replacement_score([0.0, 0.0], [1.0, 1.0])
