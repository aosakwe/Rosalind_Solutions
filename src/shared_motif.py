#!/bin/python3

#Solution to shared motif problem

import sys
from biotools import fasta_parse

reads = fasta_parse(sys.argv[1])
motif = ""

for i in len(next(iter(reads))):
	
