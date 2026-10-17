# Evidence Ledger

Project: Refined concentration inequality for sums of independent bounded random variables.
Author: Rajveersinh Vishal Pardeshi (Independent Researcher)
Date started: 2026-10-17

Status convention: Verified / Partially verified / Unverified / Contradicted / Not applicable.

---

## Claims

| ID | Exact claim | Type | Source / proof | Verification | Status | Counterevidence | Manuscript location |
|---|---|---|---|---|---|---|---|
| C1 | Two-point (tight) MGF lemma: for independent X_i in [0,1] with mean mu_i, E[e^{lambda X_i}] <= 1 + mu_i(e^lambda - 1) for lambda>=0. | Mathematical result | Derivation: convexity of e^{lambda x}; maximum over [0,1] with fixed mean attained at extreme points {0,1}. | Symbolic check + numeric spot check (Python). | Verified | None | paper/main.tex (Lemma 1) |
| C2 | Tail bound: P(S - mu >= t) <= inf_{lambda>0} exp(-lambda(mu+t)) prod_i (1 + mu_i(e^lambda - 1)). | Mathematical result | Chernoff + C1. | Derivation checked; numeric evaluation vs Monte Carlo. | Verified | None | paper/main.tex (Theorem 1) |
| C3 | Homogeneous case reduces to the Bernoulli/binomial Chernoff (Cramer) rate, the tight large-deviation rate. | Mathematical result | Known (Cramer/Sanov for Bernoulli). | Symbolic. | Partially verified (classical; cited) | None | paper/main.tex (Remark) |
| C4 | The bound is strictly tighter than Hoeffding's exp(-2 t^2 / n) in an explicit non-empty regime (low mean, moderate t). | Mathematical result | Analytic + numeric demonstration. | Numeric examples computed. | Verified (for examples) | None | paper/main.tex (Section: comparison) |
| C5 | Monte Carlo validation: empirical tail probability never exceeds the computed bound across tested parameter settings. | Experimental result | Python simulation (src/concentration.py). | 10^6 trials per setting, multiple settings. | Verified | None | results/, paper/main.tex |
| C6 | Literature: the two-point MGF / tight Hoeffding lemma is classical (Hoeffding 1963); Bennett (1962) gives the variance-aware family; the Bernoulli worst-case MGF and sharper-than-Hoeffding low-mean bounds appear in standard notes ([Kakade]). The assembled explicit corollary with quantified Hoeffding-gap is at most an incremental refinement; its exact prior appearance is unconfirmed and not asserted. | Literature fact | Hoeffding (1963) [publisher+JSTOR verified]; Bennett (1962) [JSTOR verified]; BLM (2013) [OUP+OpenAlex verified]; [Kakade] lecture notes (public PDF). | Verified bibliographic records for H63, B62, BLM13. Full-text not accessed for H63/B62 (paywalled); records confirm title/authors/journal/year/pages/DOI. | Verified | None that contradict; the core is confirmed classical. | research/literature_review.md, research/novelty_assessment.md |
