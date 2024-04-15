import os
import shutil

try:
    with open('differed.txt', 'r') as file:
        paths = [line.split(' - ')[0] for line in file if line.strip()]

    for path in paths:

        if os.path.isabs(path):
            abs_path = path
        else:
            abs_path = os.path.abspath(path)

        dest_path = os.path.join('GENERATED', abs_path.lstrip('/'))

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        shutil.copy2(abs_path, dest_path)

except Exception as e:
    print(str(e))
