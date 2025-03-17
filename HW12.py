import sys

def parse_fasta(file_content):
    """
    Parses a FASTA file into a dictionary of sequence IDs and their corresponding DNA strings.
    
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

def construct_overlap_graph(sequences, k=3):
    """
    Constructs the overlap graph for DNA strings where an edge (A, B) exists if 
    the suffix of length k of A matches the prefix of length k of B.

    Parameters:
    sequences (dict): Dictionary of sequence IDs mapped to DNA strings.
    k (int): Length of the overlap (default is 3).

    Returns:
    list: A list of tuples representing the adjacency list (ID_A, ID_B).
    """
    adjacency_list = []
    sequence_items = list(sequences.items())

    for id_A, seq_A in sequence_items:
        suffix_A = seq_A[-k:]  # Last k characters of sequence A
        for id_B, seq_B in sequence_items:
            if id_A != id_B and suffix_A == seq_B[:k]:  # Avoid self-loops
                adjacency_list.append((id_A, id_B))

    return adjacency_list

# Read the input FASTA file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    fasta_content = file.read()

# Parse the FASTA sequences
sequences = parse_fasta(fasta_content)

# Construct the adjacency list
adjacency_list = construct_overlap_graph(sequences, k=3)

# Print the adjacency list
for edge in adjacency_list:
    print(edge[0], edge[1])
