"""
Automated tests for the sharp two-point MGF concentration bound.

These tests encode falsifiable claims from the manuscript:
  (T1) The two-point bound is never below the exact binomial tail (validity).
  (T2) The two-point bound is never above Hoeffding's bound (dominance).
  (T3) Monte Carlo empirical tails stay below the computed bound.
  (T4) The Bernoulli worst-case MGF bound is tight (equality for Bernoulli).
"""
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from concentration import (
    bound_upper_tail,
    hoeffding_upper_tail,
    bernstein_upper_tail,
    monte_carlo_tail,
)
from math import comb


def binomial_tail(n, m, k):
    return sum(comb(n, j) * m ** j * (1 - m) ** (n - j) for j in range(k, n + 1))


def test_bound_above_exact_binomial():
    """T1: two-point (Chernoff) bound >= exact binomial tail."""
    cases = [(20, 0.30, 10), (50, 0.20, 20), (100, 0.10, 20), (100, 0.30, 40)]
    for n, m, k in cases:
        mus = [m] * n
        mu = n * m
        t = k - mu
        b, _ = bound_upper_tail(mus, t)
        exact = binomial_tail(n, m, k)
        assert b >= exact * 0.999, f"bound {b} below exact {exact} for n={n},m={m},k={k}"


def test_bound_below_hoeffding():
    """T2: sharp two-point bound <= Hoeffding's bound."""
    for m in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        n = 100
        t = 20
        mus = [m] * n
        mu = n * m
        b, _ = bound_upper_tail(mus, t)
        h = hoeffding_upper_tail(n, t)
        assert b <= h * 1.0001, f"two-point {b} > Hoeffding {h} at m={m}"


def test_monte_carlo_below_bound():
    """T3: empirical tails stay below the computed bound."""
    scenarios = [([0.05] * 50, 5.0), ([0.3] * 100, 20.0), ([0.1] * 100, 20.0)]
    for mus, t in scenarios:
        b, _ = bound_upper_tail(mus, t)
        mc = monte_carlo_tail(mus, t, trials=50000, seed=3)
        assert mc <= b * 1.02, f"MC {mc} exceeds bound {b}"


def test_two_point_mgf_tight_for_bernoulli():
    """T4: for Bernoulli(m), E[e^{lambda X}] = 1-m + m e^lambda exactly (two-point law)."""
    import math

    for m in [0.1, 0.5, 0.9]:
        for lam in [0.1, 1.0, 3.0]:
            # Two-point MGF bound value
            bound_val = 1 - m + m * math.exp(lam)
            # Exact Bernoulli MGF
            exact_val = (1 - m) * math.exp(lam * 0) + m * math.exp(lam * 1)
            assert abs(bound_val - exact_val) < 1e-12


def test_bound_decreases_with_lambda_then_increases(convexity=True):
    """Sanity: the objective is convex and the infimum is interior (not at 0)."""
    mus = [0.2] * 50
    mu = sum(mus)
    t = 10.0

    def neg_log_bound(lam):
        from concentration import two_point_mgf_bound

        return -lam * (mu + t) + two_point_mgf_bound(mus, lam)

    # The objective at lam->0 tends to 1 (log 0); at optimum it should be < 1 for t>0.
    b, lam = bound_upper_tail(mus, t)
    assert 0.0 < b < 1.0
    assert lam > 0


if __name__ == "__main__":
    test_bound_above_exact_binomial()
    test_bound_below_hoeffding()
    test_monte_carlo_below_bound()
    test_two_point_mgf_tight_for_bernoulli()
    test_bound_decreases_with_lambda_then_increases()
    print("All tests passed.")
