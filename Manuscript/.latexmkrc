# .latexmkrc  — build with XeLaTeX by default

# Use XeLaTeX (produces PDF)
$pdf_mode = 5;   # 5 = xelatex

# Safer, more informative runs
$interaction = 'nonstopmode';
$file_line_error = 1;
$halt_on_error = 1;

# SyncTeX for editor forward/inverse search
$pdflatex_silent = 0;
$latex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$pdflatex = $latex;  # kept for compatibility with some latexmk paths

# Bibliography tool:
# - If you use biber, keep this enabled:
$bibtex_use = 2;   # 2 = biber, 1 = bibtex, 0 = none

# Optional: put build artefacts in a separate directory (uncomment to use)
# $out_dir = '../Releases';

# Optional: enable shell-escape only if you truly need it (e.g. minted)
# $latex = 'xelatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';