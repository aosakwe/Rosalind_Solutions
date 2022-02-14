#!/bin/python3

# Solution to RNA Splicing problem
import sys
import biotools as bio

reads = bio.fasta_parse(sys.argv[1])

main_read = list(reads.keys())[0]
main_seq = reads[main_read]

for read in reads:
	if read == main_read:
		continue
	main_seq = main_seq.replace(reads[read],'')
print(bio.translate(main_seq,True))

