#!/usr/bin/python3
#Solution to GC Content Problem
import sys
if len(sys.argv) != 2:
	print("Error: program requires one fasta input file \n Usage: ./gc_count.py file")
	exit(1)
f = open(sys.argv[1], 'r')
gc_dict = {}
gc_counter = {}
for line in f:
	if line[0] == '>':
		id = line[1:].strip()
	elif id in gc_dict:
		gc_dict[id] += line.strip()
	else:
		gc_dict[id] = line.strip()
largest_gc = ["",0]
for seq in gc_dict:
	gc_counter[seq] = 100* (gc_dict[seq].count('G') + gc_dict[seq].count('C'))/len(gc_dict[seq])
	if gc_counter[seq] >= largest_gc[1]:
		largest_gc[0] = seq
		largest_gc[1] = gc_counter[seq]

print(largest_gc[0] + "\n" + "{:.6f}".format(largest_gc[1]))
f.close()
