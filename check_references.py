import re
from pathlib import Path
from typing import Set

# Config
BIB_FILE = Path('references.bib')
MANUSCRIPT_DIR = Path('manuscript')

def extract_bib_keys(bib_path: Path) -> Set[str]:
    """Extract citation keys from bibliography file."""
    keys = set()
    key_pattern = re.compile(r'@\w+\{([^,]+),')
    
    with open(bib_path, 'r', encoding='utf-8') as f:
        for line in f:
            if match := key_pattern.match(line):
                keys.add(match.group(1).strip())
    
    return keys

def extract_tex_citations(tex_dir: Path) -> Set[str]:
    """Extract citation keys from LaTeX files."""
    keys = set()
    cite_pattern = re.compile(r'\\(?:auto|paren|super|text|foot)?cite(?:\[[^\]]*\])?\{([^}]+)\}')
    
    for tex_file in tex_dir.rglob('*.tex'):
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
            for match in cite_pattern.finditer(content):
                citation_keys = [k.strip() for k in match.group(1).split(',')]
                keys.update(citation_keys)
    
    return keys

def main() -> None:
    """Check for unused and missing references in LaTeX manuscript."""
    # Extract keys from sources
    bib_keys = extract_bib_keys(BIB_FILE)
    tex_keys = extract_tex_citations(MANUSCRIPT_DIR)
    
    # Discrepancy analysis
    unused_keys = bib_keys - tex_keys
    missing_keys = tex_keys - bib_keys
    
    # Show some results
    print(f"Bibliography entries: {len(bib_keys)}")
    print(f"Citations found: {len(tex_keys)}")
    
    if unused_keys:
        print(f"\nUnused references ({len(unused_keys)}):")
        for key in sorted(unused_keys):
            print(f"  {key}")
    
    if missing_keys:
        print(f"\nMissing references ({len(missing_keys)}):")
        for key in sorted(missing_keys):
            print(f"  {key}")
    
    if not unused_keys and not missing_keys:
        print("\nAll references are properly cited.")

if __name__ == "__main__":
    main() 