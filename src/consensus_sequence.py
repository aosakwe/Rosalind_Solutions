#!/usr/bin/python3
#Solution to Consensus and profile problem
# Could be used with Chip-seq data to determine a DNA binding site of a protein

## Below can be used to make script usable in a shell pipeline
import sys
if len(sys.argv) != 2:
	print("Missing input file \n Usage: ./consensus_sequence.py file")
	exit(1)		
f = open(sys.argv[1], 'r')
#f = open('seq.txt', 'r')
strands = []
strand_length = 0
profile = []
index = 0
for line in f:
	if line[0] == '>' and len(strands) == 1:
		strand_length = len(strands[0]) #first strand is complete so we can use it as the ref length
	if line[0] == '>' and len(strands) == 0:
		strands.append("")
	elif line[0] == '>' and len(strands) == index + 1:
		strands.append("") #opens up spot in list to store new sequences
		if strand_length != len(strands[index]):
                          raise ValueError("Provided sequences must all be of equal length")
		index += 1 #shift index to new position to store values


	elif line[0] != '>':
		strands[index] += line.strip()
f.close()
for i in range(strand_length):
	base_distr = [0,0,0,0]
	for strand in strands:
		base_distr[0] += strand[i].count('A')
		base_distr[1] += strand[i].count('C')
		base_distr[2] += strand[i].count('G')
		base_distr[3] += strand[i].count('T')
	profile.append(base_distr)
consensus = []
profile_matrix = [[],[],[],[]]
for bases in profile:
	if bases[0] >= bases[1] and bases[0] >= bases[2] and bases[0] >= bases[3]:
		consensus.append('A')
	elif bases[1] >= bases[2] and bases[1] >= bases[3]:
		consensus.append('C')
	elif bases[2] >= bases[3]:
		consensus.append('G')
	else:
		consensus.append('T')
	profile_matrix[0].append(bases[0])
	profile_matrix[1].append(bases[1])
	profile_matrix[2].append(bases[2])
	profile_matrix[3].append(bases[3])

print("".join(consensus))
print("A:", *profile_matrix[0])
print("C:", *profile_matrix[1])
print("G:", *profile_matrix[2])
print("T:", *profile_matrix[3])

