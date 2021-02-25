#Solution to Consensus and profile problem
# Could be used with Chip-seq data to determine a DNA binding site of a protein
f = open('seq.txt', 'r')
strands = []
strand_length = 0
profile = []
for line in f:
	if line[0] != '>':
		if len(strands) == 0:
			strand_length = len(line.strip())
		if strand_length != len(line.strip()):
			raise ValueError("Provided sequences must all be of equal length")
	
		strands.append(line.strip())
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
print("A:", end = " ")
print(*profile_matrix[0])
print("C:", end = " ")
print(*profile_matrix[1])
print("G:", end = " ")
print(*profile_matrix[2])
print("T:", end = " ")
print(*profile_matrix[3])

