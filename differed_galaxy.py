import glob
from collections import defaultdict

try:
    files1 = glob.glob('*.ogfs')
    files2 = glob.glob('*.mgfs')

    hashes1 = defaultdict(list)
    for filename in files1:
        with open(filename, 'r') as file:
            for line in file:
                if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line:
                    path, hash = line.split(' - ')[0], line.split(' - ')[1].strip()
                    hashes1[hash].append(path)

    hashes2 = defaultdict(list)
    for filename in files2:
        with open(filename, 'r') as file:
            for line in file:
                if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line:
                    path, hash = line.split(' - ')[0], line.split(' - ')[1].strip()
                    hashes2[hash].append(path)

    diff_hashes = set(hashes2.keys()).difference(hashes1.keys())

    with open('differed.txt', 'w') as outfile:
        for hash in diff_hashes:
            for path in hashes2[hash]:
                outfile.write(path + ' - ' + hash + '\n\n')
                
except FileNotFoundError:
    print("Error: One or both output files not found.")
except PermissionError:
    print("Error: No permission to access file. Check your permissions.")
except Exception as e:
    print(str(e))
