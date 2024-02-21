with open('output1.txt', 'r') as file1, open('output2.txt', 'r') as file2:
    hashes1 = {line.split(' - ')[1].strip(): line.split(' - ')[0] for line in file1 if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line}
    hashes2 = {line.split(' - ')[1].strip(): line.split(' - ')[0] for line in file2 if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line}

diff_hashes = set(hashes2.keys()).difference(hashes1.keys())

with open('differed.txt', 'w') as outfile:
    for hash in diff_hashes:
        outfile.write(hashes2[hash] + ' - ' + hash + '\n\n')
