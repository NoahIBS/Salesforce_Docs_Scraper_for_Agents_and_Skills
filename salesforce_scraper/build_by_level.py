import json, os, re, shutil, sys


def sanitize(name):
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._ ')
    return name[:80]


def run_build_by_level(base_dir=None):
    """Erstellt by_level/ Ordner aus content/ und links_manifest.json.
    
    Args:
        base_dir: Pfad zum Output-Ordner. Falls None, wird der Standard-Pfad verwendet.
    """
    if base_dir is None:
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

    content_dir = os.path.join(base_dir, 'content')
    by_level_dir = os.path.join(base_dir, 'by_level')

    with open(os.path.join(base_dir, 'links_manifest.json')) as f:
        links = json.load(f)

    def find_md_file(hierarchy):
        if len(hierarchy) > 1:
            folder = os.path.join(content_dir, *[sanitize(h) for h in hierarchy[:-1]])
        else:
            folder = content_dir
        path = os.path.join(folder, sanitize(hierarchy[-1]) + '.md')
        return path if os.path.exists(path) else None

    copied = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    missing = 0

    for link in links:
        level = link['level']
        hierarchy = link.get('hierarchy', [link['title']])
        md_path = find_md_file(hierarchy)

        if not md_path:
            missing += 1
            continue

        level_dir = os.path.join(by_level_dir, f'L{level}')
        os.makedirs(level_dir, exist_ok=True)

        if len(hierarchy) > 1:
            prefix = '__'.join(sanitize(h) for h in hierarchy[:-1]) + '__'
        else:
            prefix = ''
        dest_name = prefix + sanitize(hierarchy[-1]) + '.md'
        shutil.copy2(md_path, os.path.join(level_dir, dest_name))
        copied[level] += 1

    print('=== By-Level Ordner erstellt ===')
    for l in sorted(copied):
        print(f'  L{l}: {copied[l]} Dateien')
    print(f'  Noch nicht gescraped: {missing}')
    print(f'  Gesamt: {sum(copied.values())} Dateien')
    print(f'\nOrdner: {by_level_dir}')
    return copied


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else None
    run_build_by_level(base)
