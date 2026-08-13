# Deliverables and File Standards

Use concise ASCII filenames. Do not overwrite prior work.

## Required for a Submission Candidate

- `CHINESE_SUMMARY.md`: motivation, exact result, proof idea, experiment summary, and cautious significance assessment.
- `PROBLEM_STATEMENT.md`: polished English problem statement with all definitions and quantifiers.
- `PROOF.md`: complete English proof, including lemmas and edge cases.
- `<short_name>.tex`: self-contained LaTeX manuscript suitable for editorial review.
- `<short_name>.pdf`: compiled and visually inspected PDF.
- `verify_<short_name>.py`: deterministic verifier with documented bounds and nonzero exit on failure.
- `LITERATURE_SEARCH.md`: exact queries, hits, equivalence audit, dates, and limitations.
- `CRUX_SUBMISSION_DRAFT.md`: proposed category, uploaded filenames, editor comment, and explicit human-only final checklist.
- `DAILY_REPORT.md`: concise daily outcome.

## LaTeX Manuscript

Include:

- title without novelty claims;
- author name and affiliation;
- statement of the problem or theorem;
- complete proof;
- optional short computational note clearly separated from proof;
- references only when verified.

Do not include private contact information in the manuscript by default.

## Verification Program

At the top of the file document:

- the statement being tested;
- Python version or dependencies if nonstandard;
- exact command;
- exhaustive bounds and randomized seed if used;
- what constitutes failure.

Print a compact final summary. Avoid output that cannot be independently interpreted.

## Package

Create a ZIP only after validation. Include the `.tex`, `.pdf`, verifier, literature log, and submission draft unless the target form requests a smaller set. Exclude auxiliary LaTeX files, temporary renders, caches, and credentials.
