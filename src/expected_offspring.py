#!/bin/env/python3

#Script for expected offsprings problem

#P(A|parental_genotype)
p_A = [1,1,1,0.75,0.5,0]

n = 2 #number of offspring

#Number of Couples
couples = [19755,18820,16024,19630,17051,18686]
expected = []
for i in range(6):
  expected.append(couples[i]*n*p_A[i])
  
print(sum(expected))
