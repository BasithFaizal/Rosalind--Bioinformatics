import sys

# Read the input file containing the DNA sequence
seq = "".join(open(sys.argv[1]).read().split())

# Initialize a dictionary to store the counts
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Iterate through the sequence and count the occurrences of each nucleotide
for n in seq:
    if n in count:
        count[n] += 1

# Print the counts for 'A', 'C', 'G', and 'T'
print(count['A'], count['C'], count['G'], count['T'])
