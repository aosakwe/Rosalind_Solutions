#!/bin/python3

##Script to solve permutation problem
import sys
import math
n = int(sys.argv[1])
 
val = [*range(1,n+1)]
print(math.factorial(n))
def permute(val,perm,ref):
	#print(val)
	if not val:
		#print(val)
		print(' '.join(map(str,perm)))
		return()
	
	for v in ref:
		perm.append(v)
		val.remove(v)
		permute(val.copy(),perm.copy(),val.copy())
		perm.remove(v)
		val.append(v)
		
permute(val,[],val.copy())
	


