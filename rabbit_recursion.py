#Code to Solve Rabbit problem

n = int(input("Number of months: "))
k = int(input("Number of pairs of rabbits produced by a pair: "))
prev = 0 #previous month's population
temp = 0 #temporary value
cur = 1 # current month's population
for i in range(n-1):
	temp = cur + k*prev
	prev = cur
	cur = temp
	print(cur)

	

