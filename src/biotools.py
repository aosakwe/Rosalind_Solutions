#!/usr/bin/python3
#Module package inspired from Rosalind problems
#Functions stored here implement frequently used methods/steps



############### Reference Dictionaries or Variables ##############
codon = {"AUU":'I' ,"AUC":'I', "AUA":'I', "CUU":'L' , "CUC" : 'L', "CUA": 'L', "CUG": 'L', "UUA": 'L', "UUG": 'L',"GUU":'V', "GUC":'V', "GUA":'V', "GUG":'V',"UUU":'F',"UUC":'F',"AUG":'M',"UGU":'C',"UGC":'C',"GCU":'A',"GCC":'A', "GCA":'A', "GCG":'A',"GGU":'G',"GGC" :'G',"GGA" :'G',"GGG" :'G',"CCU":'P',"CCC":'P',"CCA":'P',"CCG":'P',"ACU":'T',"ACC":'T',"ACA":'T',"ACG":'T',"UCU":'S',"UCC":'S',"UCA":'S',"UCG":'S',"AGU":'S',"AGC":'S',"UAU":'Y',"UAC":'Y',"UGG":'W',"CAA":'Q',"CAG":'Q',"AAU":'N',"AAC":'N',"CAU":'H',"CAC":'H',"GAA":'E',"GAG":'E',"GAU":'D',"GAC":'D',"AAA":'K',"AAG":'K',"CGU":'R',"CGC":'R',"CGA":'R',"CGG":'R',"AGA":'R',"AGG":'R',"UAA":"STOP","UAG":"STOP","UGA":"STOP"}
amino_acid = {}
protein_mass = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
protein_polarity = {}    

############# Functions #####################
def fasta_parse(file_path): ## parses a fasta file and stores each read into a  dictionary
	reads = {}
	f = open(file_path, 'r')
	for line in f:
		if line[0] == '>':
			id = line[1:].strip()
			reads[id] = ""
		else:
			reads[id] += line.strip()
	f.close()
	return reads
			
		
def complementary_seq(seq): # Returns the complementary sequence of a DNA strand with 5' to 3' orientation

    complement = []

    for i in range(len(seq)-1,-1,-1):
        if seq[i] == 'A':
            complement.append('T')
        elif seq[i] == 'C':
            complement.append('G')
        elif seq[i] == 'G':
            complement.append('C')
        elif seq[i] == 'T':
            complement.append('A')
    return "".join(complement)
  
  
def dnacount(seq):   #Count number of nucleotides
    count = [0,0,0,0] #A C G T
    for i in seq:
            if i == 'A':
                count[0] += 1
            elif i =='C':
                count[1] += 1
            elif i == 'G':
                count[2] += 1
            elif i =='T':
                count[3] += 1
            else:
                raise ValueError("invalid nucleotide found")
    return count


def transcribe(seq):
    for i in range(len(seq)):
            seq = list(seq)
            if seq[i] != 'A'  and seq[i] != 'C' and seq[i] != 'G' and seq[i] != 'T':
                    raise ValueError("Invalid Nucleotide detected")
            if seq[i] == 'T':
                    seq[i] = 'U'
    return "".join(seq)


def translate(seq, DNA = False):
    protein = []
    if DNA:
        seq = transcribe(seq)
    i = 0
    while seq[i:i+3] != "AUG":
            i = i + 1
    protein.append(codon[seq[i:i+3]])
    i += 3
    while i+3 <= len(seq):
            if seq[i:i+3] not in codon:
                    raise ValueError("Codon:" + seq[i:i+3] + " does not exist")
            if codon[seq[i:i+3]] == "STOP":
              return "".join(protein)
            else:
              
                    protein.append(codon[seq[i:i+3]])
                    i += 3
    return ''


def point_mutations(seq1,seq2):
    if len(seq1) != len(seq2):
            raise ValueError("Sequences do not have the same length")
    count = 0
    for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                    count += 1
    return count


def gc_count(seq):
    return 100* (seq.count('G') + seq.count('C'))/len(seq)

def orf_finder(seq, DNA = True):
	orfs = []
	for i in range(len(seq)):
		if i+3 < len(seq):	
			if DNA and seq[i:i+3] == "ATG":
				orfs.append(i)
			elif seq[i:i+3] == "AUG" and not DNA:
				orfs.append(i)
		else:
			return orfs
	return orfs
    
