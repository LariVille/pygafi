import os
import shutil

with open('differed.txt', 'r') as file:
    paths = [line.split(' - ')[0] for line in file if line.strip()]

for path in paths:
    abs_path = os.path.abspath(path)

    _, rel_path = os.path.splitdrive(abs_path)

    dest_path = os.path.join('GENERATED', rel_path.lstrip('\\'))

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    shutil.copy2(path, dest_path)
