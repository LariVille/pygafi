# pygafi
*Python Galaxy Files.*

> This project is still in **BETA**, if you find any problems, please report them in the issues tab.

# What is Pygafi?
Pygafi is a Python tool used to compare two Super Mario Galaxy (2) file systems.
It can extract modified data from a file system based on the original.

# Requirements

Before you can use this tool, please make sure you have the following software installed:
* [Python 3.9.0](https://www.python.org/) or newer

For Linux users only:
* [Python 3.9.0](https://www.python.org/) or newer
* sha256sum (mostly preinstalled on every Linux Distro)
* realpath

# How to use Pygafi
## General Information
If you are on Windows, use the `.bat` files in the Windows-Output-Generator folder.

If you are on Linux, use the `.sh` files in the Linux-Output-Generator folder.

## Generate output files
### Get original output

First of all, you need a clean Super Mario Galaxy (2) file system using the unmodified version of the game.
(The content extracted from your ISO must be on a known file path).

Copy `diff_galaxy_og.bat`/`diff_galaxy_og.sh` into `\DATA\files\` and run it. **(It must be the original file system!)**
It should generate a file called `output1.txt` containing the hash of each file (SHA-256) with a path linked to it.

Once the operation is complete, copy `output1.txt` into the same folder as `differed_galaxy.py`.

### Get the modified output

After obtaining `output1.txt`, it's time to generate another output file.
You'll need the modified file system from your Super Mario Galaxy (2) Rom-Hack.

Copy `diff_galaxy_modded.bat`/`diff_galaxy_modded.sh` into `\DATA\files\` and run it. **(It must be the modified file system!)**
It should generate a file called `output2.txt` containing the hash of each file (SHA-256) with a path linked to it.

Once the operation is complete, copy `output2.txt` to the same folder as `differed_galaxy.py`.

## Analyze output file differences

Go to the pygafi root folder, make sure there are `output1.txt` *(the original)* and `output2.txt` *(the modified)*, **do not rename the files**.

Run `differed_galaxy.py` and it will generate `differed.txt` containing all the hash differences between the two outputs.

Do not rename or move `differed.txt` until you finished using Pygafi.

## Extract modified data

Finally, make sure the modified file system is still connected to the device and run `generate.py`/`generate_linux.py`.

A folder called `GENERATED` will contain all the data extracted from the modified file system.

# FAQ

Q: When i'm generating an output file I get an error saying that a file is empty and it was ignored, should I be concerned?

A: No, it's totally normal, some files in the original Super Mario Galaxy (2) File System are empty, it won't modify the result.


Q: When i'm trying to run the `.sh` files, it says access denied or no permission what should I do?

A: You need to set the `.sh` files as an executable by entering `chmod +x [name of the file].sh` in the console. (Without the brackets)


# Known Bugs

* The content extracted in LocalizeData may be incorrect due to regional differences
