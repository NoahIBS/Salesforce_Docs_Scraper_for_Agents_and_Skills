import os, shutil

base = '/Users/noahhigazi/Desktop/Data_Quality_&_Gathering/salesforce_scraper/output'
src = os.path.join(base, 'by_level')
dst = os.path.join(base, 'by_level_L1_L3')

if os.path.exists(dst):
    shutil.rmtree(dst)

for level in ['L1', 'L2', 'L3']:
    src_level = os.path.join(src, level)
    dst_level = os.path.join(dst, level)
    if os.path.exists(src_level):
        shutil.copytree(src_level, dst_level)
        print(f'  {level}: {len(os.listdir(dst_level))} Dateien')

total = sum(len(os.listdir(os.path.join(dst, l))) for l in ['L1','L2','L3'])
print(f'Gesamt: {total} Dateien')
print(f'Ordner: {dst}')
