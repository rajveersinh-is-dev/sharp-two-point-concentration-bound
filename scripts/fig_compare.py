"""
Generate Figure 1: two-point bound vs Hoeffding vs exact binomial vs Monte Carlo
across mean m (n=100, t=20). Saves figures/fig1_compare.pdf and .png.
"""
from math import comb
import math, os, sys

from src.concentration import bound_upper_tail, hoeffding_upper_tail, monte_carlo_tail
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

n = 100
t = 20
ms = [0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
two_pt, hoeff, bern, mc_vals, exact = [], [], [], [], []

for m in ms:
    mus = [m] * n
    mu = n * m
    q = m + t / n
    v = n * m * (1 - m)
    b, _ = bound_upper_tail(mus, t)
    h = hoeffding_upper_tail(n, t)
    be = math.exp(-(t * t) / (2.0 * (v + t / 3.0)))
    mc = monte_carlo_tail(mus, t, trials=60000, seed=7)
    D = q * math.log(q / m) + (1 - q) * math.log((1 - q) / (1 - m))
    ex = sum(comb(n, j) * m ** j * (1 - m) ** (n - j) for j in range(math.ceil(n * q), n + 1))
    two_pt.append(b); hoeff.append(h); bern.append(be); mc_vals.append(mc); exact.append(ex)

os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures"), exist_ok=True)

plt.figure(figsize=(6.4, 4.2))
plt.semilogy(ms, two_pt, "o-", label="Two-point (Cramér) bound")
plt.semilogy(ms, hoeff, "s--", label="Hoeffding")
plt.semilogy(ms, mc_vals, "D:", label="Monte Carlo (1e5 trials)")
plt.semilogy(ms, exact, "v-.", label="Exact binomial tail")
plt.xlabel("Bernoulli mean m")
plt.ylabel("Tail probability P[S >= n(m+0.2)]")
plt.title("n=100, deviation t=20 (q=m+0.2); log scale")
plt.grid(True, which="both", ls=":", alpha=0.5)
plt.legend(fontsize=8, loc="upper left")
plt.tight_layout()
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
plt.savefig(os.path.join(outdir, "fig1_compare.pdf"))
plt.savefig(os.path.join(outdir, "fig1_compare.png"), dpi=150)
plt.close()
print("Figure saved to figures/fig1_compare.pdf/.png")
