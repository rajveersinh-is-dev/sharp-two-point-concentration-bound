"""
Refined concentration inequality for sums of independent [0,1]-valued
random variables, based on the tight (two-point) Hoeffding MGF bound.

For independent X_i in [0,1] with mean mu_i = E[X_i]:
    E[exp(lambda X_i)] <= 1 + mu_i (exp(lambda) - 1)   (lambda >= 0)
(the maximum over all distributions on [0,1] with fixed mean mu_i is
attained by the two-point law on {0,1}; convexity of exp).

Hence, for S = sum X_i, mu = E[S], and any t >= 0:
    P(S >= mu + t) <= inf_{lambda>0} exp(-lambda (mu + t))
                     * prod_i (1 + mu_i (exp(lambda) - 1)).

This is the tight range-based Chernoff bound. In the homogeneous case
(mu_i = m all i) it equals the Bernoulli/binomial Cramer rate, i.e. the
tight large-deviation rate; it is strictly tighter than Hoeffding's
exp(-2 t^2 / n) whenever the means are not all 1/2.

The script:
  (a) computes the bound by one-dimensional convex minimisation over lambda,
  (b) compares it to Hoeffding and Bernstein,
  (c) validates it against Monte Carlo simulation,
  (d) demonstrates a parameter regime where it beats Hoeffding.
"""
import math
from bisect import bisect_left

# ---------------------------------------------------------------------------
# Core bound
# ---------------------------------------------------------------------------

def two_point_mgf_bound(mus, lam):
    """prod_i (1 + mu_i (e^lam - 1)) computed stably in log space."""
    em1 = math.expm1(lam)  # e^lam - 1, accurate for small lam
    logp = 0.0
    for m in mus:
        # 1 + m (e^lam - 1) > 0 for m in [0,1], lam >= 0
        logp += math.log(1.0 + m * em1)
    return logp


def bound_upper_tail(mus, t):
    """inf_{lam>0} exp(-lam (mu + t)) prod_i (1 + mu_i (e^lam - 1))."""
    mu = sum(mus)
    n = len(mus)

    def neg_log_bound(lam):
        # log of the RHS = -lam(mu+t) + sum log(1 + m_i (e^lam - 1))
        return -lam * (mu + t) + two_point_mgf_bound(mus, lam)

    # Convex in lam; minimise by golden-section on [lo, hi].
    lo, hi = 1e-12, 100.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    for _ in range(200):
        x1 = hi - gr * (hi - lo)
        x2 = lo + gr * (hi - lo)
        f1, f2 = neg_log_bound(x1), neg_log_bound(x2)
        if f1 > f2:
            lo = x1
        else:
            hi = x2
    lam = 0.5 * (lo + hi)
    return math.exp(neg_log_bound(lam)), lam


def hoeffding_upper_tail(n, t):
    return math.exp(-2.0 * t * t / n)


def bernstein_upper_tail(v, t):
    # variables in [0,1]: |X_i - mu_i| <= 1, use b-a = 1
    return math.exp(-(t * t) / (2.0 * (v + t / 3.0)))


# ---------------------------------------------------------------------------
# Monte Carlo validation
# ---------------------------------------------------------------------------

import random


def monte_carlo_tail(mus, t, trials, seed=0):
    """Estimate P(S >= mu + t) by sampling X_i ~ Bernoulli(mu_i)
    (the two-point worst case, so if the bound holds here it is tight)."""
    random.seed(seed)
    n = len(mus)
    mu = sum(mus)
    threshold = mu + t
    count = 0
    for _ in range(trials):
        s = 0.0
        for m in mus:
            s += 1.0 if random.random() < m else 0.0
        if s >= threshold:
            count += 1
    return count / trials


# ---------------------------------------------------------------------------
# Demonstration
# ---------------------------------------------------------------------------

def demonstrate():
    print("=" * 70)
    print("Refined (two-point MGF) concentration bound - demonstration")
    print("=" * 70)

    scenarios = [
        # (description, mus, t)
        ("low mean, small n", [0.05] * 10, 1.5),
        ("low mean, larger n", [0.05] * 50, 5.0),
        ("mid mean (Hoeffding tight case)", [0.5] * 10, 2.0),
        ("heterogeneous means", [0.1, 0.2, 0.05, 0.3, 0.02] * 4, 3.0),
        ("very low mean", [0.01] * 100, 3.0),
    ]

    print(f"\n{'scenario':<28} {'t':>6} {'two-pt':>10} {'Hoeff.':>10} {'Bernst.':>10} {'MC':>8} {'bound valid?':>12}")
    print("-" * 70)
    for desc, mus, t in scenarios:
        n = len(mus)
        v = sum(m * (1.0 - m) for m in mus)  # Bernoulli variance
        b, lam = bound_upper_tail(mus, t)
        h = hoeffding_upper_tail(n, t)
        bern = bernstein_upper_tail(v, t)
        mc = monte_carlo_tail(mus, t, trials=200000, seed=42)
        valid = mc <= b * 1.005  # small Monte Carlo slack
        print(f"{desc:<28} {t:>6.1f} {b:>10.6f} {h:>10.6f} {bern:>10.6f} {mc:>8.5f} {str(valid):>12}")
        print(f"{'':<28} {'lambda*':>6} {lam:>10.4f} {'mu':>10} {sum(mus):>10.3f} {'V':>10} {v:>10.3f}")

    # Explicit improvement demonstration: low mean
    print("\n--- Explicit regime where two-point bound beats Hoeffding ---")
    mus = [0.05] * 50
    t = 5.0
    n = len(mus)
    v = sum(m * (1.0 - m) for m in mus)
    b, lam = bound_upper_tail(mus, t)
    h = hoeffding_upper_tail(n, t)
    print(f"n={n}, mu_i=0.05, mu={sum(mus):.2f}, V={v:.3f}, t={t}")
    print(f"  two-point bound = {b:.8f}")
    print(f"  Hoeffding       = {h:.8f}")
    print(f"  ratio Hoeff/two-pt = {h/b:.4f}  (two-point is {h/b:.2f}x smaller)")
    print(f"  Bernstein       = {bernstein_upper_tail(v, t):.8f}")

    # Homogeneous Bernoulli -> matches Cramer rate (sanity: binomial tail)
    print("\n--- Homogeneous Bernoulli vs exact binomial tail (n=20, m=0.3) ---")
    from math import comb
    n, m, k = 20, 0.3, 10
    mus = [m] * n
    t = k - n * m
    b, _ = bound_upper_tail(mus, t)
    exact = sum(comb(n, j) * m ** j * (1 - m) ** (n - j) for j in range(k, n + 1))
    print(f"  Cramer/two-point bound = {b:.8f}")
    print(f"  exact Binomial(n=20,p=0.3) P(X>=10) = {exact:.8f}")
    print(f"  bound >= exact (valid, tight): {b >= exact}")


if __name__ == "__main__":
    demonstrate()
