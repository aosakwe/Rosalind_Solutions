#!/bin/python3
#Code to Solve Mortal Rabbits problem

n = int(input("Number of months: "))
m = int(input("Lifespan of rabbits: "))

def mortalfib(n,m):
	if n == 1 or n == 2:
		return 1
	elif n < 1:
		return 0
	elif n <= m:
		return mortalfib(n-1,m) + mortalfib(n-2,m)
	elif n == m+1:
		return mortalfib(n-1,m) + mortalfib(n-2,m) - 1
	else:
		return mortalfib(n-1,m) + mortalfib(n-2,m) - mortalfib(n-m-1,m)
print(mortalfib(n,m) + 1)
	

