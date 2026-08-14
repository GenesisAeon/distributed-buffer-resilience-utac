"""The Glacier Buffer Replacement (GBR) score.

OPTIONAL / SPECULATIVE module -- READ THIS BEFORE USING ANYTHING BELOW.

GBR is NOT a peer-reviewed, published metric. It is this ecosystem's
own discretized implementation of a formula P102.md itself proposes as
its own synthesis (not a literature citation) for scoring how much of a
drought-period flow deficit a set of adaptation measures actually
closes. Same honesty pattern as glacier-buffer-replacement-utac (P100)'s
Resilience Replacement Factor -- see RRF_NOT_PEER_REVIEWED_WARNING
there for the analogous precedent.
"""

from __future__ import annotations

from collections.abc import Sequence

GBR_NOT_PEER_REVIEWED_WARNING = (
    "The Glacier Buffer Replacement (GBR) score is NOT a peer-reviewed "
    "or published metric. It is a discretized implementation of a "
    "formula P102.md proposes as its own synthesis, built on top of "
    "this ecosystem's real, verified drought/streamflow data -- but the "
    "scoring formula itself carries no primary citation. Do not present "
    "GBR outputs as a measured or literature-validated quantity."
)


def glacier_buffer_replacement_score(
    deficit_without_adaptation: Sequence[float],
    flow_gain_from_adaptation: Sequence[float],
) -> float:
    """Speculative GBR = sum(min(gain[t], deficit[t])) / sum(deficit[t]) over a drought period.

    See GBR_NOT_PEER_REVIEWED_WARNING. Both sequences must be the same
    length, one value per time step across the drought/heat period
    being evaluated:

    - deficit_without_adaptation[t]: D(t), the flow deficit (versus a
      no-deficit baseline) that WOULD exist without any adaptation
      measures at time t. Must be >= 0.
    - flow_gain_from_adaptation[t]: the additional flow (Q_adaptive(t)
      - Q_no_adaptation(t)) contributed by the adaptation portfolio
      (reservoirs, MAR, wetlands, demand management, ...) at time t.
      May be negative (adaptation measures can occasionally reduce
      flow, e.g. reservoir filling).

    Returns 1.0 for full compensation of the defined deficit -- capped
    there by construction, since each term is min(gain, deficit) <=
    deficit, so overshooting gain in one period cannot offset
    undershooting in another (matching P102.md's own integral
    definition). Can go negative if the adaptation portfolio nets out
    to REDUCING flow during the deficit period (e.g. reservoir filling
    at the wrong time) -- that is a real, meaningful failure mode, not
    a bug, and is deliberately not clamped to zero.
    """
    if len(deficit_without_adaptation) != len(flow_gain_from_adaptation):
        raise ValueError(
            "deficit_without_adaptation and flow_gain_from_adaptation must "
            f"have equal length, got {len(deficit_without_adaptation)} and "
            f"{len(flow_gain_from_adaptation)}"
        )
    if len(deficit_without_adaptation) == 0:
        raise ValueError("input sequences must be non-empty")
    if any(d < 0 for d in deficit_without_adaptation):
        raise ValueError("deficit_without_adaptation values must all be non-negative")

    total_deficit = sum(deficit_without_adaptation)
    if total_deficit == 0:
        raise ValueError(
            "sum(deficit_without_adaptation) is zero -- GBR is undefined "
            "with no deficit to compensate"
        )
    compensated = sum(
        min(gain, deficit)
        for deficit, gain in zip(deficit_without_adaptation, flow_gain_from_adaptation, strict=True)
    )
    return compensated / total_deficit
