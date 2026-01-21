# <Book Title>

A 450-page book on research: how it works, how to do it well, and how to stay constructively critical without losing the joy.

## What’s in this repository
- `/Manuscript/` — LaTeX source

## Build the book (XeLaTeX)

This project is built with **XeLaTeX**.

We recommend `latexmk`:

```sh
cd manuscript
latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex

## How to read
Download the latest release from the GitHub “Releases” page.

## Licence
The book text and figures are licensed under: CC BY-NC-ND 4.0 (share widely, no changes, no commercial reuse)
See `LICENSE`.

Code/scripts (if any) are licensed under: MIT (or Apache-2.0).
See `LICENSE-CODE`.

## Support
If you’d like to help us keep improving the book — including an audio version and short video support for the more complex parts —
you can support us here: http://buymeacoffee.com/jonlucia.

## Contributing
We welcome material contributions, but **please contact us before you start** so we can coordinate (scope, style, attribution, and where it fits).
See `CONTRIBUTING.md`.

## Citation
- BibTeX: `CITATION.bib`
- GitHub citation metadata: `CITATION.cff`
