#!/bin/env/python3

#Solution to Shared motif problem
from biotools import fasta_parse

fasta = fasta_parse("./datasets/rosalind_lcsm.txt")

#Solution
#Can create a dictionary with every possible substring of the first string
#Then find the substrings which occur in ALL strings
#Select the largest substring that remains

#Building suffix Dictionary
sub_reads = {}
ref_read = list(fasta.keys())[0]
for i in range(len(fasta[ref_read])):
  for j in range(i+1,len(fasta[ref_read])):
    sub_reads[fasta[ref_read][i:j]] = 1
    
#Counting occurences
for read in fasta.keys():
  if read == ref_read:
    continue
  for sub_read in sub_reads:
      if sub_read in fasta[read]:
        sub_reads[sub_read] += 1
  print("Done " + read)

#Subset dict to only include common substrings
valid_sub =  {key: value for key, value in sub_reads.items() if value == len(fasta.keys())}

#Find longest substring
print(max(list(valid_sub.keys()),key = len))

