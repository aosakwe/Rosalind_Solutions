#!/bin/python3

#Solution to Open reading frame problem

import biotools as bio #importing script of functions I built for rosalind problems. will upload to GitHub soon.
import sys

f = bio.fasta_parse(sys.argv[1])

for read in f:
	orfs = bio.orf_finder(f[read])
	for i in orfs:
		print(bio.translate(f[read][i:],True))
