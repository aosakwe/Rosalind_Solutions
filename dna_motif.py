#Solution to DNA motif Problem

seq = input("Enter DNA sequence here: ")
motif = input("Enter motif sequence here: ")
if len(seq) < len(motif):
	raise ValueError("Motif MUST be shorter than or equal to the length of the provided DNA sequence")

for i in range(len(seq)-len(motif)):
	if seq[i:i+len(motif)] == motif:
		print(i, end = " ")
print()

