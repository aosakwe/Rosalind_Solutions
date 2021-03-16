#!/bin/python3
#Solution to find all the reverse palindromes in an input sequence
import sys
from complement import complementary_seq

f = open(sys.argv[1],'r')
seq = ""
for line in f:
	if line[0] != '>':
		seq += line.strip()
i = 0
while i + 4 <= len(seq):
	for j in [4,5,6,7,8,9,10,11,12]:
		if i + j <= len(seq):
			if "".join(seq[i:i+j]) == "".join(complementary_seq("".join(seq[i:i+j]))):
				print(str(i+1) + " " + str(j))
	i += 1
f.close()
