"""
Generate numerical results for the manuscript: improvement of the tight
two-point MGF concentration bound over Hoeffding, across means and t.
"""
import math
from src.concentration import (
    bound_upper_tail, hoeffding_upper_tail, bernstein_upper_tail,
    monte_carlo_tail,
)
from math import comb


def bernoulli_kl(q, m):
    if q <= 0 or q >= 1 or m <= 0 or m >= 1:
        return float('inf')
    return q * math.log(q / m) + (1 - q) * math.log((1 - q) / (1 - m))


def improvement_table():
    print("Improvement of two-point bound over Hoeffding (upper tail).")
    print("n=100, t fixed; vary mean m. Bernoulli variables (worst case).")
    print(f"{'m':>6} {'t':>6} {'mu':>8} {'two-pt':>10} {'Hoeff.':>10} {'ratio H/2p':>11} {'MC':>8} {'valid'}")
    print("-" * 70)
    n = 100
    for m in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        mus = [m] * n
        mu = n * m
        t = int(round(0.2 * n))  # t = 0.2 n -> q = m + 0.2
        q = m + t / n
        b, lam = bound_upper_tail(mus, t)
        h = hoeffding_upper_tail(n, t)
        mc = monte_carlo_tail(mus, t, trials=100000, seed=7)
        print(f"{m:>6.2f} {t:>6d} {mu:>8.2f} {b:>10.6e} {h:>10.6e} {h/b:>11.3f} {mc:>8.5f} {str(mc <= b*1.01):>5}")

    # Explicit relative entropy exponent vs Hoeffding exponent
    print("\nRelative-entropy exponent D(q||m) vs Hoeffding exponent 2(q-m)^2 (n=1).")
    print(f"{'m':>6} {'q':>6} {'D(q||m)':>10} {'2(q-m)^2':>10} {'ratio':>8} {'strict Hoeffding gap?'}")
    print("-" * 60)
    for m in [0.01, 0.05, 0.1, 0.2, 0.5]:
        q = min(m + 0.15, 0.99)
        D = bernoulli_kl(q, m)
        hoef_exp = 2 * (q - m) ** 2
        print(f"{m:>6.2f} {q:>6.2f} {D:>10.6f} {hoef_exp:>10.6f} {D/hoef_exp:>8.3f}")


def binomial_tightness():
    """Two-point bound vs exact binomial tail for several (n,m,k)."""
    print("\nHomogeneous Bernoulli: two-point (Cramer) bound vs exact binomial tail.")
    print(f"{'n':>5} {'m':>6} {'k':>5} {'bound':>12} {'exact':>12} {'bound>=exact':>14}")
    print("-" * 55)
    for n, m, k in [(20, 0.3, 10), (50, 0.2, 20), (100, 0.1, 20), (100, 0.3, 40)]:
        mus = [m] * n
        mu = n * m
        t = k - mu
        b, _ = bound_upper_tail(mus, t)
        exact = sum(comb(n, j) * m ** j * (1 - m) ** (n - j) for j in range(k, n + 1))
        print(f"{n:>5} {m:>6.2f} {k:>5} {b:>12.6e} {exact:>12.6e} {str(b >= exact):>14}")


def lower_tail_check():
    """Lower tail via symmetry: P(S <= mu - t) = P(S' >= mu' + t) with S' = n - S."""
    print("\nLower-tail check (Bernoulli m=0.05, n=50, t=5):")
    mus = [0.05] * 50
    n = 50
    mu = n * 0.05
    t = 5.0
    # P(S <= mu - t) = P(n - S >= n - mu + t) = P(S' >= mu' + t), S'=n-S, mu'=n-mu, X'_i=1-X_i ~ Bernoulli(1-m)
    mus2 = [1.0 - m for m in mus]
    mu2 = n - mu
    b, _ = bound_upper_tail(mus2, t)
    mc = monte_carlo_tail(mus2, t, trials=100000, seed=11)
    print(f"  bound P(S' >= mu'+t) = {b:.6e}")
    print(f"  MC estimate           = {mc:.6f}")
    print(f"  valid: {mc <= b * 1.01}")


if __name__ == "__main__":
    improvement_table()
    binomial_tightness()
    lower_tail_check()
