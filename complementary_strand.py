
seq = list(input("Enter a DNA sequence to complement: "))

complement = []

for i in range(len(seq)-1,-1,-1):
	if seq[i] == 'A':
		complement.append('T')
	elif seq[i] == 'C':
		complement.append('G')
	elif seq[i] == 'G':
		complement.append('C')
	elif seq[i] == 'T':
		complement.append('A')
print("5'-" + "".join(complement) + "-3'")
