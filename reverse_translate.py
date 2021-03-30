#!/bin/python3

#Solution to Finding Number of possible RNA strings for a given Protein Sequence

#import sys
from biotools import codon as Codons

protein = input("Enter protein sequence: ")
possible_codons = []
for i in range(len(protein)):
	possible_codons.append(0)
	for codon in Codons:
		if Codons[codon] == protein[i]:
			possible_codons[i] += 1
	if possible_codons[i] == 0:
		raise ValueError("Error: Input sequence has invalid amino acid identities")
x = 3 
#print(possible_codons)
for combinations in possible_codons:
	x = x*combinations
print(x%1000000)
