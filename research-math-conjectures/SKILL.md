---
name: research-math-conjectures
description: Explore simple conjectures in elementary number theory, combinatorics, recurrence sequences, graph theory, and elementary algebra; test them computationally, prove or refute them rigorously, perform bounded novelty searches, produce reproducible LaTeX/PDF submission materials, and optionally stage a Crux submission for human confirmation. Use for requests such as 每天寻找数学猜想, 严格证明或反驳, 数学结果查重, 生成可投稿材料, or 把 Crux 页面填写到待确认状态.
---

# Research Math Conjectures

## Purpose

Run a quality-first mathematical research workflow from exploration through a human-gated submission package. Treat computation as evidence, never as proof. Make conservative claims about novelty and publication value.

## Non-Negotiable Rules

1. Never call finite verification a proof.
2. Label a result `可投稿候选` only after producing a complete, stepwise, human-checkable proof or disproof.
3. Never claim “first”, “new”, “novel”, “previously unknown”, or equivalent. Report only the databases, queries, dates, matches, and limitations of the search.
4. If the statement is known, an obvious reformulation, already solved, too routine, or the proof has a gap, label it `不可投稿` and explain why.
5. Prefer one defensible candidate over many weak candidates. If none passes every gate, report `今日未发现可投稿候选`.
6. Do not invent citations, search results, computations, PDF checks, or browser actions.
7. Never tick an originality, copyright, authorship, or author-responsibility declaration for the user.
8. Never click `Finish`, `Submit`, `Publish`, send an email, or perform any equivalent irreversible publication action. Stop at the pending-confirmation state.

Read [references/submission-safety.md](references/submission-safety.md) before opening or changing any submission page. Read [references/author-profile.md](references/author-profile.md) only when preparing submission metadata or filling a form. Do not put the email address in the public manuscript unless the user explicitly requests it.

## Set Up the Run

1. Locate the workspace and inspect existing `outputs/` material to avoid duplicating prior candidates.
2. Create a non-overwriting dated directory with:

   ```bash
   python3 <skill-directory>/scripts/new_research_run.py --output-root <workspace>/outputs
   ```

3. Use the returned directory for all user-facing artifacts. Keep scratch programs, downloads, and intermediate renders outside that directory until validated.
4. Record the local date, timezone, candidate title, exact statement, and status in `DAILY_REPORT.md`.

If the task is a one-off proof audit rather than a daily search, preserve the same evidence and status gates but create only the artifacts the user requested.

## Explore Candidate Families

Explore several independent, elementary families before selecting one. Favor statements with:

- definitions explainable in a few lines;
- meaningful edge cases and a nontrivial equality or extremal structure;
- a feasible exhaustive or randomized test;
- a proof path using elementary tools;
- an unexpected connection, not merely a cosmetic identity.

Good sources include gcd/lcm identities, divisibility and valuations, residue classes, finite sums and products, lattice or graph invariants, recurrence behavior, and extremal set configurations.

For every explored family, record:

- the exact quantified statement and domain;
- motivating examples;
- why it might be true;
- the first plausible proof strategy;
- the first plausible failure mode.

Reject tautologies, direct substitutions into famous theorems, parameter renamings, and claims whose “surprise” disappears after a one-line standard identity unless the resulting problem still has genuine standalone value.

## Run Computational Experiments

Write a reproducible verification program before investing in a long proof.

1. Test boundary cases separately: zero if allowed, one, smallest graph/order, repeated values, equality cases, and degenerate parameters.
2. Use exhaustive enumeration where the state space permits it; otherwise combine a documented finite range with seeded randomized or adversarial tests.
3. Search actively for counterexamples, not only confirming examples.
4. Cross-check delicate arithmetic with an independent formulation where practical.
5. Record environment, command, range, count of cases, seed, runtime if material, and result.
6. Keep the reusable final verifier as `verify_<short_name>.py` and ensure it exits nonzero on failure.

Do not describe a range as “large” without giving the actual bound and number of tested cases.

## Prove or Refute

Write the proof independently of the program.

1. State all definitions and domain restrictions.
2. Separate lemmas from the main theorem when they carry real logical weight.
3. Justify every implication, division, cancellation, parity step, extremal choice, and induction transition.
4. Audit empty, singleton, equality, sign, and ordering cases.
5. Verify that the proof establishes the exact quantified statement tested by the program.
6. Try to break the proof by reversing key implications, testing equality conditions, and constructing near-counterexamples.

Use one of these statuses:

- `可投稿候选`: rigorous proof/disproof complete, experiments reproducible, bounded novelty search complete, manuscript visually checked.
- `未解决`: promising statement but proof or disproof incomplete.
- `不可投稿`: duplicate/near-duplicate, routine restatement, counterexample invalidates intended claim, proof gap, or insufficient publication value.

## Perform a Bounded Novelty Search

Search the exact structure, not just the proposed title. Consult [references/search-protocol.md](references/search-protocol.md) and create `LITERATURE_SEARCH.md`.

At minimum attempt:

- OEIS for associated integer sequences;
- arXiv and OpenAlex for formulas, keywords, and theorem structure;
- publicly accessible zbMATH results;
- Google Scholar or exact-phrase web searches;
- relevant olympiad, contest, problem-column, and recreational-math archives.

For each source, record the access date, exact queries, useful hits, why each hit is or is not equivalent, and access limitations. If a source is blocked or unavailable, say so and lower confidence. Search common equivalent formulations, parameter substitutions, contrapositives, and stronger known theorems.

Conclude with bounded language such as: “No exact match was found in the searches listed below; this limited search does not establish originality.”

## Build the Candidate Package

For a `可投稿候选`, produce the files specified in [references/deliverables.md](references/deliverables.md). Copy templates from `assets/` when helpful.

Required core files:

- Chinese research summary;
- English problem statement;
- complete English proof;
- standalone LaTeX source;
- compiled PDF;
- reproducible verification program;
- literature-search log;
- Crux submission draft;
- daily report.

Compile the LaTeX source and fix every compilation error or material warning. Use the PDF skill when available, render every page, and visually inspect clipping, equations, page breaks, symbols, metadata, and blank pages. State “visually checked” only after actual page inspection.

Package only validated submission files. Do not include scratch notes, browser downloads, credentials, or unverified claims.

## Stage a Crux Submission

Only stage the form when the current user request explicitly authorizes form filling or upload. Invocation of this skill alone does not authorize transmitting personal data or files.

1. Read [references/submission-safety.md](references/submission-safety.md) and [references/author-profile.md](references/author-profile.md).
2. Verify the manuscript category against the current form. A new standalone problem generally uses a proposal category; a response to an existing numbered problem uses the matching solution category.
3. Fill author fields, select the category, upload the validated `.tex` and `.pdf`, add the verifier if accepted, and write a concise comment identifying the submitted problem.
4. Confirm upload completion and visually inspect the populated page.
5. Leave every declaration checkbox unchecked.
6. Do not click the final action button. Stop and report exactly what is filled, what is uploaded, what remains unchecked, and what the user must review and submit.

## Report the Daily Outcome

Complete `DAILY_REPORT.md` even when no candidate survives. Include:

- today's candidate statement;
- proof status;
- experiment range and outcome;
- novelty-search outcome and limitations;
- publication-value judgment;
- generated absolute file paths;
- whether a submission page was staged;
- the user's next step.

Lead with the status. Distinguish clearly between mathematical correctness, search confidence, editorial suitability, and actual submission state.

## Resources

- `scripts/new_research_run.py`: create a dated, non-overwriting output folder and starter logs.
- `references/search-protocol.md`: novelty-search checklist and equivalence audit.
- `references/deliverables.md`: required filenames and content standards.
- `references/submission-safety.md`: mandatory browser and publication boundary.
- `references/author-profile.md`: local submission metadata supplied by the user.
- `assets/DAILY_REPORT_TEMPLATE.md`: daily outcome template.
- `assets/LITERATURE_SEARCH_TEMPLATE.md`: bounded search-log template.
- `assets/CRUX_SUBMISSION_TEMPLATE.md`: form comment and submission-note template.
