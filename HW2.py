import sys

# Read the input file containing the DNA sequence
seq = "".join(open(sys.argv[1]).read().split())

# Transcribe DNA to RNA by replacing 'T' with 'U'
rna = seq.replace('T', 'U')

# Print the transcribed RNA string
print(rna)


