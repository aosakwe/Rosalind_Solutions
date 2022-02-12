#!/usr/bin/python3

## Solution to Overlap Graphs Problem on Rosalind
import sys
from biotools import fasta_parse

fasta = fasta_parse(sys.argv[1])

completed = []

for read1 in fasta:
  completed.append(read1)
  for read2 in fasta:
      if fasta[read1] == fasta[read2] or read2 in completed:
        continue
      else:
        if fasta[read1][0:3] == fasta[read2][len(fasta[read2])-3:len(fasta[read2])]:
          print(read2 + " " + read1)
        elif fasta[read1][len(fasta[read1])-3:len(fasta[read1])] == fasta[read2][0:3]:
          print(read1 + " " + read2)
