# pygafi
<h3 align="center">
  <br>
  <img src="https://github.com/LariVille/pygafi/blob/main/logo.png" alt="Pygafi logo"/>
  <br>
  <b>Python Galaxy Files</b>
  <br>
</h3>

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

### The instructions have been moved to the [Wiki](https://github.com/LariVille/pygafi/wiki)

# FAQ

Q: When i'm generating an output file I get an error saying that a file is empty and it was ignored, should I be concerned?

A: No, it's totally normal, some files in the original Super Mario Galaxy (2) File System are empty, it won't modify the result.


Q: When i'm trying to run the `.sh` files, it says access denied or no permission what should I do?

A: You need to set the `.sh` files as an executable by entering `chmod +x [name of the file].sh` in the console. (Without the brackets)


# Known Bugs

* Extracted localization data may be incorrect due to regional differences.
(For instance, if your modified NTSC-U file system includes PAL translations alongside NTSC-U translations, and you are using an unmodified NTSC-U file system, only the NTSC-U translations will be correctly extracted. The PAL translations won’t be sorted and will be considered modified, as the NTSC-U version doesn’t inherently have PAL translations. However, PAL translations will always be present in the extraction, which contains the original game files. A patch to address this issue will be available soon.).
