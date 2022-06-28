# ReNumb
Renumbers a PDB protein structure starting at residue 1, atom 1, or chain A

## Description
If you have a .pdb file with a protein structure where the first residue does NOT start at the number 1 this script renumbers the .pdb file as to have the first residue start at 1. This makes using this file in computation much easier. It can also renumber atoms to start at 1, and chains to start at A.

## How to use:
Run using the following command:

`python3 ReNumb.py FILENAME.pdb CHOICE`

Where CHOICE can be atom, residue, or chain 

The script will generate a new file with the name renumbered_FILENAME.pdb
