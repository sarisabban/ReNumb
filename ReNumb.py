#!/usr/bin/python3

import sys

def Motif(filename):
	''' Renumbers a PDB structure '''
	''' Generates a new file with the prefix _renumbered '''
	pdb = open(filename , 'r')
	NewFile = open(filename.split('.')[0] + '_renumbered.pdb' , 'w')
	count = 0
	num = 0
	AA2 = None
	for line in pdb:
		if not line.startswith('ATOM'):			#Ignore all lines that do not start with ATOM
			continue
		else:
			count += 1				#Sequencially number atoms
			AA1 = line[23:27]			#Sequencially number residues
			if not AA1 == AA2:
				num += 1			
			final_line = line[:7] + '{:4d}'.format(count) + line[11:17] + line[17:21] + 'A' + '{:4d}'.format(num) + line[26:]	#Update each line of the motif to have its atoms and residues sequencially labeled, as well as being in chain A
			AA2 = AA1
			NewFile.write(final_line)			#Write to new file called motif.pdb
	NewFile.close()


Filename = sys.argv[1]
Motif(Filename)
