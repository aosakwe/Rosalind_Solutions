#!/usr/bin/python3
#Script to count number of point mutations between two sequences of equal length

seq1 = input("Enter initial sequence: ")
seq2 = input("Enter second sequence: ")
if len(seq1) != len(seq2):
	raise ValueError("Sequences do not have the same length")

count = 0
for i in range(len(seq1)):
	if seq1[i] != seq2[i]:
		count += 1
print(count)
