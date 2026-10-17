# Novelty Assessment

**Author:** Rajveersinh Vishal Pardeshi (Independent Researcher)
**Date:** 2026-10-17

## Classification

**Incremental / expository — novelty not established for the underlying inequalities.**

The proposed work is a self-contained, explicitly verified refinement of the classical Hoeffding concentration inequality. Every mathematical ingredient is established in the literature:

- The sharp two-point (convexity/chord) MGF bound for a bounded variable with known mean is the argument underlying Hoeffding's lemma in Hoeffding (1963).
- The Chernoff/Cramer minimization over lambda is the standard large-deviation method (Chernoff 1952; Boucheron, Lugosi & Massart 2013).
- The fact that Bernoulli (two-point) variables are the worst case for the MGF, and that this yields bounds sharper than Hoeffding in the low-mean regime, is already stated in standard teaching notes ([Kakade] 2020) and is implicit in the Bernoulli Chernoff bound.

The limited, verifiable elements that go beyond simply restating Hoeffding's inequality are:

1. **Assembling** the sharp two-point MGF into an explicit infimum-form tail bound (Theorem 1) rather than stating only the e^{lambda^2/8} relaxation.
2. **Quantifying the strict improvement over Hoeffding** via the relative-entropy gap D(q||m) > 2(q-m)^2 (strict Pinsker) for the homogeneous Bernoulli case, with the improvement factor shown to be unbounded as m -> 0 (Corollary 1).
3. **Numerical verification** with reproducible code (fixed seed): Monte Carlo validation, comparison to Hoeffding/Bernstein, tightness against exact binomial tails.

These are real and verified, but they are refinements of classical material, not a new fundamental inequality.

## Why this classification over the alternatives

- **Not "strongly supported originality":** the central inequality is classical (Hoeffding 1963); searching found the essential idea in multiple sources.
- **Not merely "potentially novel":** the classical status of the core is confirmed, so uncertainty about novelty is low in the direction of "already known," not high in the direction of "new."
- **Incremental is the honest label:** the work extends the presentation/quantification of an established approach in a limited, clearly-scoped way, with full proofs and verification.

## What is genuinely new (narrowly scoped)

- The explicit assembled Theorem 1 + Corollary 1 in this exact form (sharp infimum bound + relative-entropy Hoeffding-gap corollary), as far as my search found.
- The reproducible numerical demonstration and comparison tables.
- The honest, source-by-source novelty disclosure in this document and the literature review.

## Claims I deliberately do NOT make

- That this is the first, only, or groundbreaking concentration inequality.
- That the two-point MGF bound or the Bernoulli Chernoff bound is new.
- That the bound is state-of-the-art relative to all modern concentration results (e.g., Bentkus, Talagrand refinements exist).

## Evidence

See research/evidence_ledger.md (claims C1-C6) and research/literature_review.md (comparison table). Verification status: mathematical derivation verified symbolically; numerical results verified by code; novelty status = classical roots confirmed, assembled-form novelty uncertain and not asserted.
