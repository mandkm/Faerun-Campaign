#!/usr/bin/env python3
import os
from datetime import datetime

ROOT = '.'
# Dateien/Ordner hier ausschließen (z.B. '.git')
EXCLUDE = {'.git'}


def generate_listing(path, indent=0):
    lines = []
    try:
        entries = sorted(os.listdir(path), key=lambda s: s.lower())
    except PermissionError:
        return lines
    for name in entries:
        if name in EXCLUDE:
            continue
        full = os.path.join(path, name)
        rel = os.path.relpath(full, ROOT)
        prefix = '  ' * indent + '- '
        if os.path.isdir(full):
            # Link auf Verzeichnis (mit / am Ende)
            lines.append(f"{prefix}[{name}]({rel}/)")
            lines.extend(generate_listing(full, indent+1))
        else:
            lines.append(f"{prefix}[{name}]({rel})")
    return lines


if __name__ == '__main__':
    header = "# Index\n\n> Diese Datei wird automatisch generiert.\n\n"
    header += f"Stand: {datetime.utcnow().isoformat()} UTC\n\n"
    lines = generate_listing(ROOT, 0)
    content = header + '\n'.join(lines) + '\n'
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(content)
