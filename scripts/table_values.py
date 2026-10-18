"""Print table rows (seed 7, 1e5 trials) to copy into the manuscript."""
import math, os, sys

from src.concentration import bound_upper_tail, hoeffding_upper_tail, monte_carlo_tail
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

n = 100
t = 20
for m in [0.01, 0.05, 0.10, 0.20, 0.30, 0.50]:
    mus = [m] * n
    mu = n * m
    v = n * m * (1 - m)
    b, _ = bound_upper_tail(mus, t)
    h = hoeffding_upper_tail(n, t)
    be = math.exp(-(t * t) / (2.0 * (v + t / 3.0)))
    mc = monte_carlo_tail(mus, t, trials=100000, seed=7)
    ratio = h / b
    print(f"{m:.2f} & {mu:.2f} & {b:.2e} & {h:.2e} & {ratio:.2e} & {mc:.5f} \\\\")
