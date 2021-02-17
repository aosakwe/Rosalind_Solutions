seq = list("ACGT")

for i in range(len(seq)): 
	if seq[i] == 'T':
		seq[i] = 'U'
print("".join(seq))
