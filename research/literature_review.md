# Literature Review

**Project:** Refined concentration inequality for sums of independent bounded random variables (sharp two-point MGF / Chernoff bound; explicit improvement over Hoeffding).
**Author:** Rajveersinh Vishal Pardeshi (Independent Researcher)
**Date:** 2026-10-17

## Search strategy

- Searched for the classical sources of concentration inequalities for sums of bounded random variables: Hoeffding (1963), Bennett (1962), Chernoff (1952).
- Searched for modern textbook treatments: Boucheron, Lugosi & Massart (2013), *Concentration Inequalities* (OUP).
- Searched for explicit statements of the worst-case/two-point moment-generating-function bound and of bounds sharper than Hoeffding in the low-mean regime (e.g., university lecture notes).
- Searched candidate publication venues (Oxford University Press journals) and their author instructions / fee policies.

Sources were located via publisher pages (Taylor & Francis / Oxford Academic), JSTOR, OpenAlex, and Google Books. Where a full text was not accessible, the bibliographic record (title, authors, journal, year, volume, issue, pages, DOI) was taken from the publisher/Crossref/OpenAlex record and is marked accordingly.

**Limitation acknowledged:** Literature searches are incomplete by nature. Absence of a discovered reference does not prove absolute originality. The comparison below is based on the sources actually located; earlier or adjacent formulations may exist that were not found.

## Principal sources consulted

| # | Citation | Access status | Notes |
|---|----------|---------------|-------|
| [H63] | W. Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables," *Journal of the American Statistical Association*, 58(301):13-30, 1963. DOI: 10.1080/01621459.1963.10500830. JSTOR stable 2282952. | Publisher abstract + JSTOR record verified; full text paywalled | Classical source of Hoeffding's lemma (MGF <= exp(lambda^2 (b-a)^2/8)) and Hoeffding's inequality. The proof uses the convexity/two-point (chord) MGF bound, then relaxes it. |
| [B62] | G. Bennett, "Probability Inequalities for the Sum of Independent Random Variables," *JASA*, 57(297):33-45, 1962. DOI: 10.2307/2282438. JSTOR stable 2282438. | Publisher/JSTOR record verified | Variance-aware exponential bound (Bennett/Bernstein family). |
| [C52] | H. Chernoff, "A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the Sum of Observations," *Annals of Mathematical Statistics*, 23(4):493-509, 1952. DOI: 10.1214/aoms/1177729330. | Classic; bibliographic record (Ann. Math. Stat.) | Origin of the Chernoff/Cramer large-deviation method. |
| [BLM13] | S. Boucheron, G. Lugosi, P. Massart, *Concentration Inequalities: A Nonasymptotic Theory of Independence*, Oxford University Press, 2013. ISBN 978-0-19-953525-5. DOI: 10.1093/acprof:oso/9780199535255.001.0001. | OUP + OpenAlex verified | Modern textbook; treats the Chernoff method and bounded-differences bounds. |
| [Kakade] | S. Kakade, "Stat 928: Statistical Learning Theory," Lecture 6 (Hoeffding, Chernoff, Bennett, Bernstein bounds), University of Washington, 2020. | Lecture notes (PDF), publicly accessible | Explicitly states worst-case MGF for X in [0,1] is Bernoulli(mu), and gives bounds sharper than Hoeffding when mu is small (multiplicative Chernoff form). Non-peer-reviewed teaching notes. |

## Literature comparison table

| Reference | Research question | Main result / method | Assumptions & limitations | Relationship to proposed work | Exact difference claimed by proposed work | Evidence supporting that difference |
|-----------|-------------------|----------------------|---------------------------|------------------------------|-------------------------------------------|--------------------------------------|
| [H63] Hoeffding 1963 | Tail bounds for sums of independent bounded variables depending on range endpoints and mean/variance. | Hoeffding's lemma E[e^{lambda(X-mu)}] <= exp(lambda^2 (b-a)^2/8); Hoeffding's inequality P <= exp(-2 t^2 / Delta_n). | Independent, bounded summands. The e^{lambda^2/8} form is a relaxation of the sharp two-point bound. | The sharp two-point MGF bound used in my Lemma 1 is the convexity (chord) bound that underlies Hoeffding's proof. | I retain the sharp two-point MGF (no e^{lambda^2/8} relaxation), giving an explicit tail bound that is strictly tighter than Hoeffding's inequality whenever means are not all at midpoints, and quantify the gap via relative entropy. | Verified numerically: bound <= Hoeffding in all tests, strictly tighter for low/heterogeneous means (up to ~1e6 x at m=0.05). The two-point bound itself is present in Hoeffding's proof (classical). |
| [B62] Bennett 1962 | Exponential tail bounds using variance as well as range. | Bennett inequality exp(-(v^2/M^2) theta(eps M/v^2)); implies Bernstein. | Independent, bounded, variance known. | Same family (Chernoff-method exponential bounds for bounded sums). | Bennett optimizes using variance directly; my bound optimizes using the sharp per-variable two-point MGF given only mean and range. Both are valid; mine is a different (range-mean) specialization. | Both bounds are valid Chernoff-method bounds; comparison shown numerically (Bernstein/Bennett sometimes tighter than the sharp Hoeffding form depending on regime). |
| [C52] Chernoff 1952 | Asymptotic efficiency of hypothesis tests based on sums; large-deviation method. | Chernoff bound / Cramer rate via moment-generating functions. | Sums of i.i.d. observations; asymptotic setting. | The minimization over lambda (Cramer/Chernoff method) is the technique used in my Theorem 1. | I apply it non-asymptotically to independent non-identical bounded variables with the sharp two-point MGF, and give an explicit finite-n corollary. | Standard large-deviation method; finite-n application is direct. |
| [BLM13] Boucheron et al. 2013 (OUP) | Non-asymptotic theory of concentration for functions of independent variables. | Textbook treatment: Chernoff method, bounded differences, sub-Gaussian bounds. | Graduate-level monograph; broad survey. | Provides the modern framing (sub-Gaussian, bounded differences) that my result refines in the bounded scalar case. | Explicit scalar sharp bound + quantified strict improvement over Hoeffding + numerical verification. | BLM is a survey/textbook; does not state my exact assembled corollary with the quantified Hoeffding gap. |
| [Kakade] Lecture notes 2020 | Teaching concentration bounds. | Worst-case MGF for X in [0,1] is Bernoulli(mu); multiplicative Chernoff sharper than Hoeffding for small mu. | Teaching notes; Bernoulli/[0,1] setting. | Closest antecedent: already notes the worst-case Bernoulli MGF and sharper-than-Hoeffding bounds for low mu. | My work: general [a_i,b_i] independent (not just Bernoulli), full proof, explicit corollary with quantified relative-entropy gap, numerical verification, reproducible code. | Notes are non-peer-reviewed; confirm the worst-case-MGF idea is known in the teaching literature. |

## Novelty-relevant checks performed

- Equivalent theorem statements: the sharp two-point MGF bound appears in Hoeffding (1963) via the convexity/chord argument and in [Kakade] notes as the Bernoulli worst-case MGF. No exact match found for my assembled Theorem 1 + Corollary 1 (sharp infimum form + explicit relative-entropy gap + numerical verification) as a single stated result, but every ingredient is classical.
- Earlier proofs of the intended result: the convexity proof of the two-point MGF bound is in Hoeffding (1963); the Chernoff optimization is standard ([C52], [BLM13]).
- Closely related algorithms: none (this is a bound, not an algorithm).
- Known counterexamples: none to the validity of the bound; the bound is valid but conservative relative to exact tails (standard Chernoff prefactor gap).
- Special cases implying the result: the homogeneous Bernoulli case (Corollary 1) is the classical binomial Chernoff/Cramer bound.
- Prior papers containing the essential idea: Hoeffding (1963), Bennett (1962), [BLM13]; the teaching notes [Kakade].
- Negative results / impossibility: pairwise independence alone does not give exponential concentration (known); not directly relevant since I assume full independence.
- Corrections/retractions: none found for the core sources.

## Limits of the novelty search

The search was broad but not exhaustive (no full subscription-database sweep of every probability journal). The core mathematics is confirmed classical. Whether the precise assembled corollary (sharp infimum form + explicit relative-entropy Hoeffding-gap quantification + numerical verification) has appeared verbatim elsewhere is uncertain. I therefore classify the contribution as **incremental / expository** (see research/novelty_assessment.md), and I do not claim novelty of the underlying inequalities.
