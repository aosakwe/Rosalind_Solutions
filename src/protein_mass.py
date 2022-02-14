#!/bin/python3

#Script to calculate protein mass
#Rounds to 3 d.p.
import sys
from biotools import protein_mass

pmass = 0

protein = sys.argv[1]

for i in range(len(protein)):
	pmass += protein_mass[protein[i]]

print(round(pmass,3))


