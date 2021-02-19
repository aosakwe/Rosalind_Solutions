#Solution to RNA to Protein problem
#Code is set up such that we check each ORF to find a START codon before translating the sequence
codon = {"ATT": 'I' ,"ATC": 'I', "ATA" : 'I',"CTT": 'L' , "CTC" : 'L', "CTA": 'L', "CTG": 'L', "TTA": 'L', "TTG": 'L',"GTT":'V', "GTC":'V', "GTA":'V', "GTG":'V',"TTT":'F',"TTC":'F',"ATG":'M',"TGT":'C',"TGC":'C',"GCT":'A',"GCC":'A', "GCA":'A', "GCG":'A',"GGT":'G',"GGC" :'G',"GGA" :'G',"GGG" :'G',"CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',"ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',"TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',"AGT":'S',"AGC":'S',"TAT":'Y',"TAC":'Y',"TGG":'W',"CAA":'Q',"CAG":'Q',"AAT":'N',"AAC":'N',"CAT":'H',"CAC":'H',"GAA":'E',"GAG":'E',"GAT":'D',"GAC":'D',"AAA":'K',"AAG":'K',"CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',"AGA":'R',"AGG":'R'"TAA":"STOP","TAG":"STOP","TGA":"STOP"}
protein = []
seq = Input("Enter RNA Sequence")
i = 0
while seq[i:i+3] != "AUG":
	i += 1
protein.append(codon[seq[i:i+3]])
i += 3
while i+3 <= len(seq):
	if seq[i:i+3] not in codon:
		raise ValueError("Codon does not exist")
	elif seq[i:i+3] == "STOP":
		break
	protein.append(codon[seq[i:i+3]])
	i += 3
print("".join(protein))
		
