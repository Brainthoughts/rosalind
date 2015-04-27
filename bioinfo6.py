__author__ = 'hannes'

f = open('bioinfo7-seq.fasta', 'r')
seqs = {}
prefixes = {}
postfixes = {}
gc_contents = {}
max_gc_content = 0.0
max_gc_content_id = ""
current_seq = ""
current_key = f.readline()[1::].strip()
p_length = 3


def calculate_gc_content(s):
    s = s.strip()
    return (s.count('C') + s.count('G')) / len(s) * 100


def process_seq(k, s):
        global max_gc_content_id, max_gc_content
        seqs[k] = s
        prefixes[k] = s[:p_length]
        postfixes[k] = s[-p_length:]
        gc_content = calculate_gc_content(s)
        gc_contents[k] = gc_content
        if max_gc_content < gc_content:
            max_gc_content_id = k
            max_gc_content = gc_content


for line in f:
    if line.startswith('>'):
        process_seq(current_key, current_seq)
        current_key = line[1::].strip()
        current_seq = ""
    else:
        current_seq += line.strip()

process_seq(current_key, current_seq)

for i in postfixes:
    for j in prefixes:
        if postfixes[i] == prefixes[j] and i != j:
            print(i, j)

print(max_gc_content_id)
print(max_gc_content)
