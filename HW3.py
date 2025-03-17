import sys

# Read the input file containing the DNA sequence
seq = "".join(open(sys.argv[1]).read().split())

# Define the complement mapping for DNA nucleotides
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Compute the reverse complement
reverse_complement = "".join(complement[n] for n in reversed(seq))

# Print the reverse complement
print(reverse_complement)
