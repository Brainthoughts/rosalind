__author__ = 'hannes'

'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)

ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

order = ['A', 'C', 'G', 'T']
matrix = []
consensus_seq = None

def process_sequence(seq):
    global consensus_seq
    if consensus_seq is None:
        consensus_seq = list(seq)
    global matrix
    seq_index = 0
    for na in seq:
        if len(matrix) < seq_index+1:
            matrix.append([0, 0, 0, 0])
        matrix[seq_index][order.index(na)] += 1
        max_na = max(enumerate(matrix[seq_index]), key=lambda x: x[1])[0]
        consensus_seq[seq_index] = order[max_na]
        seq_index += 1


def parse_fasta(f, fun):
    seqs = {}
    current_seq = ""
    for line in f:
        if line.startswith('>'):
            current_key = line[1::].strip()
            seqs[current_key] = current_seq
            if len(current_seq) > 0:
                fun(current_seq)
                current_seq = ""
        else:
            current_seq += line.strip()
    # process last sequence
    fun(current_seq)
    return seqs


def print_output(m):
    for i, na in enumerate(order):
        na_list = [na + ":"]
        for l in matrix:
            na_list.append(l[i])
        print(' '.join(str(d) for d in na_list))

#f = open('consensus_and_profile.fasta', 'r')
f = open('rosalind_cons.txt', 'r')

parse_fasta(f, process_sequence)
print(''.join(consensus_seq))
print_output(matrix)