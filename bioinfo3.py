__author__ = 'hannes'

dna = "AAAACCCGGT"
trTable = dna.maketrans('ATGC', 'TACG')
complement = dna[::-1]
complement = complement.translate(trTable)
print(dna)
print(complement)