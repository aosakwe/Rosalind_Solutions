#code for transcribing input DNA sequence
seq = list(input("Enter a DNA sequence to transcribe: "))

for i in range(len(seq)):
	if seq[i] != 'A'  and seq[i] != 'C' and seq[i] != 'G' and seq[i] != 'T':
		raise ValueError("Invalid Nucleotide detected") 
	if seq[i] == 'T':
		seq[i] = 'U'
print("".join(seq))
