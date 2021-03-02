#!/bin/python3
#Code to Solve Mortal Rabbits problem
#Can trace number of rabbits that have lived for m months by running a second algorithm delayed by m months
#doesn't work as the tracking of m old pop also needs to account for deaths
n = int(input("Number of months: "))
m = int(input("Lifespan of rabbits: "))
prev = 0 #previous month's population
temp = 0 #temporary value
cur = 1 # current month's population
prevd = 0 
tempd = 0
curd = 1
counter = 0 
for i in range(n-1):
	temp = cur + prev
	prev = cur
	cur = temp
	counter += 1
	if counter == m:
		cur -= 1
	elif counter > m:
		tempd = curd + prevd
		prevd = curd
		curd = tempd
		cur -= curd

print(cur)


	

