#Solution to RNA to Protein problem
#Code is set up such that we check each ORF to find a START codon before translating the sequence
#Code is too slow and oftentimes prints STOP

import sys
codon = {"AUU":'I' ,"AUC":'I', "AUA":'I', "CUU":'L' , "CUC" : 'L', "CUA": 'L', "CUG": 'L', "UUA": 'L', "UUG": 'L',"GUU":'V', "GUC":'V', "GUA":'V', "GUG":'V',"UUU":'F',"UUC":'F',"AUG":'M',"UGU":'C',"UGC":'C',"GCU":'A',"GCC":'A', "GCA":'A', "GCG":'A',"GGU":'G',"GGC" :'G',"GGA" :'G',"GGG" :'G',"CCU":'P',"CCC":'P',"CCA":'P',"CCG":'P',"ACU":'T',"ACC":'T',"ACA":'T',"ACG":'T',"UCU":'S',"UCC":'S',"UCA":'S',"UCG":'S',"AGU":'S',"AGC":'S',"UAU":'Y',"UAC":'Y',"UGG":'W',"CAA":'Q',"CAG":'Q',"AAU":'N',"AAC":'N',"CAT":'H',"CAC":'H',"GAA":'E',"GAG":'E',"GAU":'D',"GAC":'D',"AAA":'K',"AAG":'K',"CGU":'R',"CGC":'R',"CGA":'R',"CGG":'R',"AGA":'R',"AGG":'R',"UAA":"STOP","UAG":"STOP","UGA":"STOP"}
protein = []
seq = input("Enter RNA Sequence: ")
#seq = sys.argv[1]
i = 0
while seq[i:i+3] != "AUG": 
	i += 1
start = i #store index of start and end of ORF to print it alongside the translated sequence. May change to just show the indices.
protein.append(codon[seq[i:i+3]])
i += 3
while i+3 <= len(seq):
	if seq[i:i+3] not in codon:
		raise ValueError("Codon does not exist")
	elif seq[i:i+3] == "STOP":
		break
	else:
		protein.append(codon[seq[i:i+3]])
		i += 3
end = i + 3
print("Reading frame: " + seq[start:end])
print("Protein sequence: " + "".join(protein))
		
