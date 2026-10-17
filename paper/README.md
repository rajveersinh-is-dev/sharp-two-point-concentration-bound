# Paper

Manuscript source for:

**A Sharp Two-Point Moment-Generating-Function Bound for Sums of Independent Bounded Random Variables: Explicit Improvement over Hoeffding's Inequality with Numerical Verification**

Author: Rajveersinh Vishal Pardeshi (Independent Researcher)

## Files

- `main.tex` — LaTeX manuscript source (article class).
- `references.bib` — Bibliography (verified references; see `research/literature_review.md`).

## Build instructions

The manuscript uses only standard LaTeX packages:

```
article, amsmath, amssymb, amsthm, mathtools, booktabs, microtype, hyperref
```

It uses the standard `thebibliography` environment (no BibTeX run required), so a single compile suffices:

```
pdflatex main.tex
```

**Compilation status:** No LaTeX distribution (pdflatex/lualatex) is installed in this environment, so the manuscript has not been compiled here. The `.tex` source has been written carefully and checked for balanced environments, but a final compile-and-verify step remains before submission. See the final report for details.

## Citations

References use `\cite{key}` with keys matching the `\bibitem` entries in `thebibliography`:

- Hoeffding1963 — Hoeffding (1963), JASA 58(301):13–30
- Bennett1962 — Bennett (1962), JASA 57(297):33–45
- Chernoff1952 — Chernoff (1952), Ann. Math. Statist. 23(4):493–509
- Boucheron2013 — Boucheron, Lugosi & Massart (2013), OUP
- Kakade2020 — Kakade (2020), UW Stat 928 lecture notes (teaching material)

All bibliographic records were verified against publisher/OpenAlex sources (see `research/literature_review.md`).

## Status

This is a complete manuscript source. It is **not** a claim of acceptance, peer review, or publication. It has not been submitted to any journal.
