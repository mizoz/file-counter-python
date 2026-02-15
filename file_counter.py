#!/usr/bin/env python3
"""Count lines, words, and characters in files."""

import sys
from pathlib import Path


def count_file(path: Path) -> dict:
    """Count lines, words, chars in a file."""
    try:
        content = path.read_text(encoding='utf-8')
        lines = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
        words = len(content.split())
        chars = len(content)
        return {'lines': lines, 'words': words, 'chars': chars, 'path': str(path)}
    except Exception as e:
        return {'error': str(e), 'path': str(path)}


def main():
    if len(sys.argv) < 2:
        print("Usage: file_counter.py <file1> [file2] ...")
        sys.exit(1)
    
    total = {'lines': 0, 'words': 0, 'chars': 0}
    
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"Error: {arg} not found")
            continue
        
        if path.is_dir():
            for f in path.rglob('*'):
                if f.is_file():
                    result = count_file(f)
                    if 'error' in result:
                        print(f"Error: {result['error']}")
                    else:
                        print(f"{result['lines']:6d} {result['words']:6d} {result['chars']:6d} {result['path']}")
                        total['lines'] += result['lines']
                        total['words'] += result['words']
                        total['chars'] += result['chars']
        else:
            result = count_file(path)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"{result['lines']:6d} {result['words']:6d} {result['chars']:6d} {result['path']}")
                total['lines'] += result['lines']
                total['words'] += result['words']
                total['chars'] += result['chars']
    
    if len(sys.argv) > 2:
        print(f"{total['lines']:6d} {total['words']:6d} {total['chars']:6d} total")


if __name__ == "__main__":
    main()
