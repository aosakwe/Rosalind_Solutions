#!/bin/python3
#Code to Solve Mortal Rabbits problem

n = int(input("Number of months: "))
m = int(input("Lifespan of rabbits: "))

def mortalfib(n,m):
	x = [1]*100
	for i in range(2,n):
		x[i] = x[i-1] + x[i-2]
		if i >= m:
			x[i] -= x[(i-m)-1]
	return x[i]
print(mortalfib(n,m))
	

