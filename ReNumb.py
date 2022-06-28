#!/usr/bin/python3

import sys

def Motif(filename, choice='residue'):
	'''
	Renumbers the amino acids in a PDB structure, it generates a new file
	with the prefix FILENAME_renumbered.pdb
	'''
	choice = choice.lower()
	with open(filename , 'r') as f:
		with open(f'renumbered_{filename}', 'w') as F:
			count = 0
			newresid = 0
			newchain = '@'
			oldresid = None
			oldchain = None
			for line in f:
				if line.startswith('ATOM'):
					count += 1
					ATOM     =       line[ 1-1:4 ].strip()
					SERIAL   =   int(line[ 7-1:11])
					NAME     =       line[13-1:16].strip()
					ALTLOC   =       line[17-1   ].strip()
					AMINO    =       line[18-1:20].strip()
					CHAIN    =       line[22-1   ].strip()
					RESIDUE  =   int(line[23-1:26])
					INSERT   =       line[27-1   ].strip()
					X        = float(line[31-1:38])
					Y        = float(line[39-1:46])
					Z        = float(line[47-1:54])
					OCCUPY   = float(line[55-1:60])
					TEMP     = float(line[61-1:66])
					SEGMENT  =       line[73-1:76].strip()
					ELEMENT  =       line[77-1:78].strip()
					if RESIDUE != oldresid:
						newresid += 1
						oldresid = RESIDUE
					if CHAIN != oldchain:
						newchain = chr(ord(newchain) + 1)
						oldchain = CHAIN
					if choice   == 'atom': SERIAL = count
					elif choice == 'residue': RESIDUE = newresid
					elif choice == 'chain': CHAIN = newchain
					newline  = f'{ATOM}  {SERIAL:>5}  {NAME:<3}{ALTLOC:>1}'
					newline += f'{AMINO:>3} {CHAIN}'
					newline += f'{RESIDUE:>4}{INSERT:>1}   {X:>8}{Y:>8}{Z:>8}'
					newline += f'{OCCUPY:>6}{TEMP:>6}      '
					newline += f'{SEGMENT:<4}{ELEMENT:>2}'
				elif line.startswith('TER'):
					count += 1
					TER     =       line[ 1-1:4 ].strip()
					SERIAL   =   int(line[ 7-1:11])
					NAME     =       line[13-1:16].strip()
					ALTLOC   =       line[17-1   ].strip()
					AMINO    =       line[18-1:20].strip()
					CHAIN    =       line[22-1   ].strip()
					RESIDUE  =   int(line[23-1:26])
					INSERT   =       line[27-1   ].strip()
					if RESIDUE != oldresid:
						newresid += 1
						oldresid = RESIDUE
					if CHAIN != oldchain:
						newchain = chr(ord(newchain) + 1)
						oldchain = CHAIN
					if choice   == 'atom': SERIAL = count
					elif choice == 'residue': RESIDUE = newresid
					elif choice == 'chain': CHAIN = newchain
					newline  = f'{TER}   {SERIAL:>5}  {NAME:<3}{ALTLOC:>1}'
					newline += f'{AMINO:>3} {CHAIN}'
					newline += f'{RESIDUE:>4}{INSERT:>1}'
				else:
					newline = line
				F.write(newline + '\n')

Motif(sys.argv[1], choice=sys.argv[2])
