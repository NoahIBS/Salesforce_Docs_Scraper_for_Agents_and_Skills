import os, shutil, sys


def run_build_l1_l3(base_dir=None):
    """Kopiert nur L1–L3 aus by_level/ in einen eigenen Ordner.
    
    Args:
        base_dir: Pfad zum Output-Ordner. Falls None, wird der Standard-Pfad verwendet.
    """
    if base_dir is None:
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

    src = os.path.join(base_dir, 'by_level')
    dst = os.path.join(base_dir, 'by_level_L1_L3')

    if os.path.exists(dst):
        shutil.rmtree(dst)

    for level in ['L1', 'L2', 'L3']:
        src_level = os.path.join(src, level)
        dst_level = os.path.join(dst, level)
        if os.path.exists(src_level):
            shutil.copytree(src_level, dst_level)
            print(f'  {level}: {len(os.listdir(dst_level))} Dateien')

    total = sum(len(os.listdir(os.path.join(dst, l))) for l in ['L1', 'L2', 'L3'] if os.path.exists(os.path.join(dst, l)))
    print(f'Gesamt: {total} Dateien')
    print(f'Ordner: {dst}')
    return total


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else None
    run_build_l1_l3(base)
