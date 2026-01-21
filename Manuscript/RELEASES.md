# Release conventions (HRResearchHandbook)

We publish stable, reader-ready versions of the handbook via **GitHub Releases**.

## What we release
- The canonical PDF is uploaded as **`HRResearchHandbook.pdf`** (unadorned filename).
- Any companion artefacts (e.g. EPUB, slides, datasets, annexes) are uploaded alongside it.

## Naming and versioning
- We encode versioning in the **Git tag** and **Release title**, not in the PDF filename.
- Preferred tag format: `vYYYY-MM-DD` (e.g. `v2026-01-21`).
- If we need multiple releases on the same day: `vYYYY-MM-DD.1`, `vYYYY-MM-DD.2`, etc.

## Release notes (minimum)
Each release note should include:
- a short summary of what changed (high level)
- any structural changes (renamed chapters/sections)
- build details (XeLaTeX; major tooling changes if any)

## Status of the repository
The `main` branch may move ahead of the latest release. For citation and stable reading, use the latest GitHub Release.