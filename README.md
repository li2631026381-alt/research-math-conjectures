# Research Math Conjectures

A Codex skill for exploring simple mathematical conjectures, running reproducible experiments, writing human-checkable proofs or disproofs, performing bounded prior-art searches, and preparing (but never autonomously finalizing) a Crux Mathematicorum submission.

## Install

Copy the `research-math-conjectures/` directory into your Codex skills directory, or use the local installed copy at `~/.codex/skills/research-math-conjectures`.

## Use

Invoke it with:

```text
Use $research-math-conjectures to complete today's mathematics-conjecture research run.
```

The workflow treats finite computation as evidence rather than proof, reports bounded search limitations, avoids novelty claims, and stops before any originality declaration or final publication action.

## Privacy

The public copy contains a placeholder for submission email. Fill personal metadata only in a local copy and only when the user explicitly authorizes form filling.

## Contents

- `research-math-conjectures/SKILL.md` — main workflow
- `research-math-conjectures/references/` — search, deliverable, author-profile, and submission-safety guidance
- `research-math-conjectures/assets/` — daily report and Crux templates
- `research-math-conjectures/scripts/` — dated non-overwriting run initializer
