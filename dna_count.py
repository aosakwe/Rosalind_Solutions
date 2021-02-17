seq = input("Enter a DNA sequence here: ") 

count = [0,0,0,0] #A C G T
for i in seq:
	if i == 'A':
		count[0] += 1
	elif i =='C':
		count[1] += 1
	elif i == 'G':
		count[2] += 1
	elif i =='T':
		count[3] += 1
	else:
		raise ValueError("invalid nucleotide found")

print(str(count[0]) + " " + str(count[1]) + " " + str(count[2]) + " " + str(count[3]))
