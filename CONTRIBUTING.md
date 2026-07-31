# Contributing

This list indexes *other* lists. That narrow scope is the only thing that keeps it useful, so the
inclusion bar matters more here than in a typical awesome list.

## What belongs here

A repository qualifies if its **purpose is to point you at other resources** — a curated index of
tools, papers, writeups, courses or services in some security domain.

It must also be:

- **Security-focused.** General programming lists with a security section don't qualify.
- **Substantive.** Enough depth to be worth someone's time, not a dozen links in a stub README.
- **Reasonably alive, or genuinely canonical.** Dormant lists are welcome when they remain the best
  reference for their domain — several here haven't been touched in two years and still earn their
  place. What doesn't qualify is a dormant list that a maintained one supersedes.
- **Distinct.** If an existing entry already covers the same ground more thoroughly, the new one
  needs a reason to exist alongside it. Note that reason in the description.

## What doesn't

- **Individual tools.** A scanner, framework or library belongs in one of the lists we index, not
  here. Narrow exceptions exist where a tool functions as the de facto index of its domain
  (`ossf/scorecard`, `Orange-Cyberdefense/arsenal`); expect to argue the case.
- **Blogs, newsletters, courses, YouTube channels.** The list of security newsletters qualifies. An
  individual newsletter does not.
- **Uncurated dumps.** A thousand unsorted links with no organizing idea isn't curation.
- **Forks and mirrors** of lists already indexed here.

## Entry format

One line per entry:

```
- [owner/repo](https://github.com/owner/repo) — Description.
```

Then run `./scripts/refresh.py`, which appends the generated annotation:

```
- [owner/repo](https://github.com/owner/repo) — Description. — ★4.7k · 2026-01 · 💤 dormant
```

Rules:

- **Write the description yourself.** Don't paste the repository's own tagline. Say what the list
  actually covers and who should read it. Where it competes with another entry, say how it differs —
  that comparison is the value this index adds over a GitHub search.
- **Two sentences at most.** Usually one.
- **Never hand-write the `★` annotation.** It is generated. Anything after ` — ★` gets overwritten.
- **Never refer to other entries by position.** Ordering is generated, so "the list above" will
  eventually point at something else. Name the repository: ``fresher than `secfigo` ``.
- **Don't hand-sort.** `refresh.py` orders each section by star count descending. Append your entry
  anywhere in the right section and let the script place it.
- Use an em dash (` — `) between the link and the description, matching the existing entries.
- Mark non-English lists with a flag emoji and put them in the Non-English section.

## Refreshing metadata

```sh
GITHUB_TOKEN=$(gh auth token) ./scripts/refresh.py
```

The script re-queries every linked repository, rewrites the star counts, last-commit months and
`archived`/`dormant` markers, re-sorts each section, and updates the "last refreshed" date. It also
reports two things worth acting on:

- **Renamed or transferred** repositories — the GitHub API follows redirects, so the link still works
  but should be updated to the canonical name.
- **Unreachable** repositories — deleted, made private, or a network failure. Verify by hand before
  removing an entry; the script exits non-zero so CI catches it.

Without a token you get 60 requests/hour, which is not enough for a full run.

## Adding a section

Only when you have **at least two** entries that don't fit an existing one. A section with a single
entry is a sign it belongs somewhere else — the Social Engineering section is the exception, because
that domain genuinely has one serious list. Add the section to the Contents list too; anchors are
lowercased with spaces as hyphens and `&`/`,` dropped.
