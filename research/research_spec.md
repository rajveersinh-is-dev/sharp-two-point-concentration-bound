# Research Specification (internal)

Author: Rajveersinh Vishal Pardeshi (Independent Researcher)
Date: 2026-10-17
Status: Draft

## 1. Exact problem statement
Given independent random variables X_1,...,X_n with X_i in [a_i,b_i] and known means mu_i = E[X_i], derive a rigorous, explicit upper bound on
    P( sum_i X_i >= sum_i mu_i + t ),  t >= 0,
that is valid, strictly improves on Hoeffding's classical inequality whenever the means are not all at the range midpoints, and is easy to evaluate (one-dimensional convex minimisation, or a closed-form corollary in the homogeneous Bernoulli case).

## 2. Strongest relevant existing results
- Hoeffding (1963), JASA 58(301):13-30: Hoeffding's lemma E[e^{lambda(X-mu)}] <= e^{lambda^2(b-a)^2/8} and Hoeffding's inequality P <= exp(-2 t^2 / Delta_n), Delta_n = sum (b_i-a_i)^2. The proof uses the convexity (two-point/chord) MGF bound, then relaxes it to e^{lambda^2(b-a)^2/8}.
- Bennett (1962), JASA 57(297):33-45: variance-aware exponential bound.
- Boucheron, Lugosi, Massart (2013), OUP: Concentration Inequalities (textbook treatment of the Chernoff method and bounded-differences bounds).
- Standard lecture notes (e.g. Kakade, UW Stat 928): worst-case MGF for X in [0,1] is Bernoulli(mu); multiplicative Chernoff bounds sharper than Hoeffding when mu is small.

## 3. Research gap
The sharp two-point MGF bound is classical but is almost always stated only via its e^{lambda^2(b-a)^2/8} relaxation (Hoeffding's inequality). There is no commonly cited, self-contained, explicit assembled result that (a) states the sharp range-based Chernoff bound in infimum form, (b) quantifies the strict improvement over Hoeffding (the relative-entropy gap D(q||m) vs 2(q-m)^2), and (c) verifies it numerically with reproducible code. The gap is methodological/expository, not a new fundamental inequality.

## 4. Proposed contribution
- Theorem 1: sharp two-point MGF-based Chernoff (tail) bound for independent bounded variables, infimum form over lambda.
- Lemma 1: two-point (sharp Hoeffding) MGF bound, proved by convexity.
- Corollary 1: homogeneous Bernoulli case -> Cramer/relative-entropy rate exp(-n D(q||m)); strict improvement over Hoeffding's exp(-2n(q-m)^2), with D(q||m) > 2(q-m)^2 for q != m (strict Pinsker), and the improvement factor unbounded as m -> 0 with q fixed.
- Numerical verification: Monte Carlo validation, comparison to Hoeffding/Bernstein, tightness vs exact binomial tails, reproducible Python code with fixed seed.
- Honest novelty assessment: core mathematics is classical (Hoeffding 1963; Bennett 1962); contribution is the explicit assembled form, the quantified improvement gap, and verification. Classified as incremental/expository, NOT a novel theorem.

## 5. Assumptions
- X_i independent.
- a_i <= X_i <= b_i a.s.; means mu_i known; for [0,1] Bernoulli worst case, variance v_i = mu_i(1-mu_i).
- lambda > 0 for the upper tail; symmetry for the lower tail.
- Numerical results: Bernoulli variables realize the two-point worst case, so validating there is the strongest case.

## 6. Intended theorem / result
Theorem 1 (sharp Chernoff bound): P(S - mu >= t) <= inf_{lambda>0} exp(-lambda(mu+t)) prod_i (1 + mu_i (e^{lambda(b_i-a_i)}... ) ... ) [see manuscript for exact rescaled statement for [0,1]: prod_i (1 - mu_i + mu_i e^{lambda}) e^{-lambda(mu+t)}].
Corollary 1: homogeneous Bernoulli(m), P(S >= nq) <= exp(-n D(q||m)), q > m, strictly sharper than Hoeffding exp(-2n(q-m)^2).

## 7. Proof / evidence required
- Lemma 1 proof: convexity of e^{lambda x}, chord bound on [a,b], expectation uses E[X]=mu.
- Theorem 1 proof: Chernoff/Markov + independence + Lemma 1.
- Corollary 1 proof: specialize Lemma 1 to Bernoulli, optimize lambda -> Bernoulli KL/Cramer rate.
- Evidence: exact symbolic derivation; numeric tables; Monte Carlo (fixed seed); comparison vs exact binomial.

## 8. Tests that could falsify the claim
- Monte Carlo empirical tail exceeding the computed bound (would invalidate).
- Bound below the exact binomial tail (would invalidate).
- Any case where the bound is not <= Hoeffding (theory says it always is for the sharp form; check numerically).
- Code with a different seed giving a different conclusion.

## 9. Principal known limitations
- Core inequality is classical (Hoeffding 1963); novelty is at most incremental/expository.
- The infimum form requires one-dimensional numerical minimisation unless a closed-form corollary is used.
- The Chernoff bound lacks the exact prefactor (bound >= exact binomial tail, loose by a polynomial factor), as is standard for Cramer/Chernoff.
- Does not handle dependent variables (martingale extensions exist but are out of scope).

## 10. Minimum evidence to justify the abstract's claims
- The bound is valid (proved + Monte Carlo).
- The bound is strictly tighter than Hoeffding in a non-empty regime (proved via strict Pinsker + numeric tables).
- Results are reproducible (code + seed + saved output).
- Novelty is honestly disclosed as incremental/classical-roots.

## Success / failure criteria
Success: a correct, complete, self-contained manuscript with valid proofs, reproducible numerical verification, honest novelty disclosure, verified references, and a public repo.
Failure: any unchecked proof step, an invalid bound, fabricated novelty claim, or unverified citation. These would force narrowing claims or marking the work incomplete.
