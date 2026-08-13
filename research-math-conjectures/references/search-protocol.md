# Bounded Novelty Search Protocol

## Build a Query Matrix

Search multiple representations of the result:

1. exact formula with and without notation;
2. plain-language theorem statement;
3. characteristic equality or extremal condition;
4. associated integer sequence or first terms;
5. contrapositive and symmetric variants;
6. standard terminology for the proof mechanism;
7. stronger or more general theorems that imply the candidate.

## Minimum Source Log

For OEIS, arXiv, OpenAlex, public zbMATH results, Google Scholar or exact web search, and relevant problem archives, record:

- access date;
- exact query strings;
- URLs or stable identifiers for useful hits;
- result title and authors when available;
- comparison: exact, stronger, weaker, special case, related technique, or unrelated;
- access or indexing limitations.

If Google Scholar or zbMATH blocks automated access, record that limitation and use accessible primary-source or bibliographic alternatives. Never fabricate an empty result page.

## Equivalence Audit

For every close match, test:

- renamed variables or shifted indices;
- scaling by a gcd or common factor;
- dual, complement, converse, or contrapositive form;
- special case of a known identity;
- immediate corollary of a stronger theorem;
- previously published contest/problem-column version.

An “obvious variant” is not a good submission merely because its wording differs.

## Conclusion Language

Use a bounded conclusion:

> No exact match was found in the sources and queries documented here as of DATE. This search is limited by database coverage, indexing, access, terminology, and possible equivalent formulations; it does not establish originality.

State any close matches immediately after this sentence and lower the publication judgment accordingly.
