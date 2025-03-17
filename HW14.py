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

def longest_common_substring(sequences):
    """
    Find the longest common substring among a collection of DNA strings.
    
    Parameters:
    sequences (dict): Dictionary of sequence IDs mapped to DNA strings.
    
    Returns:
    str: The longest common substring.
    """
    # Get the first sequence as a reference
    reference = list(sequences.values())[0]
    max_len = len(reference)
    
    # Start with the longest possible substring and reduce size
    for length in range(max_len, 0, -1):
        for start in range(max_len - length + 1):
            substring = reference[start:start + length]
            if all(substring in seq for seq in sequences.values()):
                return substring
    
    return ""  # If no common substring is found

# Read input from file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    fasta_content = file.read()

# Parse the FASTA sequences
sequences = parse_fasta(fasta_content)

# Find and print the longest common substring
print(longest_common_substring(sequences))
