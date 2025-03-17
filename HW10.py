import sys
from collections import defaultdict

def parse_fasta(file_content):
    """
    Parse a FASTA file into a dictionary of sequence IDs and their corresponding DNA strings.
    
    Parameters:
    file_content (str): The content of the FASTA file.
    
    Returns:
    dict: A dictionary where keys are sequence IDs and values are DNA strings.
    """
    sequences = {}
    current_id = None
    for line in file_content.strip().splitlines():
        if line.startswith(">"):
            current_id = line[1:].strip()
            sequences[current_id] = ""
        else:
            sequences[current_id] += line.strip()
    return sequences

def compute_consensus_and_profile(sequences):
    """
    Compute the consensus string and profile matrix from a collection of DNA strings.
    
    Parameters:
    sequences (list): A list of DNA strings.
    
    Returns:
    tuple: The consensus string and the profile matrix as a dictionary.
    """
    length = len(sequences[0])
    profile = {base: [0] * length for base in "ACGT"}
    
    # Populate the profile matrix
    for seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1
    
    # Determine the consensus string
    consensus = ""
    for i in range(length):
        max_count = 0
        max_base = None
        for base in "ACGT":
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                max_base = base
        consensus += max_base
    
    return consensus, profile

# Read the input FASTA file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    fasta_content = file.read()

# Parse the FASTA file
sequences = list(parse_fasta(fasta_content).values())

# Compute the consensus string and profile matrix
consensus, profile = compute_consensus_and_profile(sequences)

# Print the results
print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile[base]))}")
