#Solution to Mendelian Inheritance problem

k = int(input("Number of Homozygous Dominant Individuals: "))
m = int(input("Number of Heterozygous Individuals: "))
n = int(input("Number of Homozygous Recessive Individuals: "))
if k < 0 or m < 0 or n < 0:
	raise ValueError("Input must be an integer greater or equal to 0!")
total = k + m + n
dominant_phenotype = (k/total)*((k-1)/(total-1)) + 2*(k/total)*(m/(total-1)) + 2*(k/total)*(n/(total-1))+(m/total)*((m-1)/(total-1))*3/4 + (m/total)*(n/(total-1))
print("{:.5f}".format(dominant_phenotype))

