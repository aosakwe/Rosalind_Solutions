#!/usr/bin/python3
#Solution to complementary strand problem

seq = list(input("Enter a DNA sequence to complement: "))
#seq = sys.argv[1]
def complementary_seq(seq):

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
	return complement

print("5'-" + "".join(complementary_seq(seq)) + "-3'")
