#!/usr/bin/python3
#Code to Solve Rabbit problem
#NOTE: consider implementing caches to minimize the amount of repeptitive code being run 
n = int(input("Number of months: "))
k = int(input("Number of pairs of rabbits produced by a pair: "))




def recurse(x,y):
	if x ==  2 or x == 1:
		return 1
	
	return recurse(x-1,y) + recurse(x-2,y)*y

print(recurse(n,k))
	

