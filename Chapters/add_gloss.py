import re
from pathlib import Path

# Adjust this path if glossary.bib is not in the same directory
GLOSSARY_BIB = Path("./glossary.bib")  # e.g. if script is in Chapters/ and .bib is one level up


def load_terms(bib_path: Path):
    """Parse @entry blocks and extract (label, name, plural)."""
    text = bib_path.read_text(encoding="utf-8")

    blocks = re.split(r'@entry', text)[1:]  # skip anything before the first @entry
    terms = []

    for block in blocks:
        # label
        m_label = re.search(r'\{([^,]+),', block)
        if not m_label:
            continue
        label = m_label.group(1).strip()

        # name (singular)
        m_name = re.search(r'name\s*=\s*\{([^}]*)\}', block)
        if not m_name:
            continue
        name = m_name.group(1).strip()

        # plural (if defined)
        m_plural = re.search(r'plural\s*=\s*\{([^}]*)\}', block)
        plural = m_plural.group(1).strip() if m_plural else None

        terms.append((label, name, plural))

    return terms


def make_replacers(terms):
    r"""
    For each term, build regex + replacement:
    - singular:  \gls / \Gls
    - plural:    \glspl / \Glspl  (only if plural is defined)
    The regex is designed NOT to match inside hyphenated strings
    like 'empirical-variable' or inside labels we have just created.
    """
    replacers = []

    # Sort by length of name so longer phrases (e.g. "empirical variable")
    # are replaced before shorter ones (e.g. "variable").
    def length_key(t):
        _, name, plural = t
        return max(len(name), len(plural or ""))

    for label, name, plural in sorted(terms, key=length_key, reverse=True):

        def patterns_for(base, is_plural):
            if not base:
                return []

            # We match case-insensitively against the lower-case text,
            # but require that it is not part of a longer word or hyphenated token.
            pat_lower = re.escape(base.lower())
            # custom "word boundaries": no letter/digit/hyphen immediately before or after
            regex = re.compile(
                rf'(?i)(?<![A-Za-z0-9-]){pat_lower}(?![A-Za-z0-9-])'
            )

            def repl(match):
                text = match.group(0)
                is_capital = text[0].isupper()
                if is_plural:
                    cmd = "Glspl" if is_capital else "glspl"
                else:
                    cmd = "Gls" if is_capital else "gls"
                return f"\\{cmd}{{{label}}}"

            return [(regex, repl)]

        # singular
        replacers.extend(patterns_for(name, is_plural=False))
        # plural (only if explicitly in .bib)
        if plural:
            replacers.extend(patterns_for(plural, is_plural=True))

    return replacers


def process_tex_file(path: Path, replacers):
    text = path.read_text(encoding="utf-8")

    for regex, repl in replacers:
        text = regex.sub(repl, text)

    path.write_text(text, encoding="utf-8")
    print(f"Processed {path}")


def main():
    terms = load_terms(GLOSSARY_BIB)
    print(f"Loaded {len(terms)} glossary entries")

    replacers = make_replacers(terms)

    # adjust the root folder as needed
    tex_files = sorted(Path(".").rglob("*.tex"))

    for tex in tex_files:
        process_tex_file(tex, replacers)


if __name__ == "__main__":
    main()