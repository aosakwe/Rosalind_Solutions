#!/bin/python3

#Solution to Open reading frame problem

import biotools as bio #importing script of functions I built for rosalind problems.
import sys


reads = bio.fasta_parse(sys.argv[1])
proteins = set()
for read in reads:
	orfs = bio.orf_finder(reads[read])
	for i in orfs:
		proteins.add(bio.translate(reads[read][i:],True))
	comp_seq = bio.complementary_seq(reads[read])
	comp_orfs = bio.orf_finder(comp_seq)
	for i in comp_orfs:
		proteins.add(bio.translate(comp_seq[i:],True))

print('\n'.join(proteins))
