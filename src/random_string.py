#!/bin/env python3
#Solution to Random Strings problem on Rosalind

import sys
import math
f = open(sys.argv[1], 'r')
seq = f.readline()
gc_values = (f.readline().strip()).split(sep = " ")
for value in gc_values:
	gc = float(value)/2
	at = 0.5 - gc
	print("{:.3f}".format(math.log(gc**(seq.count('G')+seq.count('C'))*at**(seq.count('A')+seq.count('T')),10)), end = " ")	
f.close()
print()
