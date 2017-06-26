# ReNumb
Renumbers a PDB protein structure starting at residue 1 and chain A

## Description
If you have a .pdb file with a single protein domain where the first residue does NOT start at the number 1 this script renumbers the .pdb file as to have the first residue start at 1 and chain A. This makes using this file in computation much easier.

## How to use:
1. the script and the .pdb file should be in the same working directory.
2. Run using the following command:

`python3 ReNumb.py FILENAME.pdb`

3. The script will generate a new file with the prefix _renumbered.
