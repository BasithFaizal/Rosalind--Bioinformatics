import sys

def count_rna_strings(protein_string):
    # Codon possibilities for each amino acid
    codon_map = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2,
        'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2,
        'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2
    }
    
    # Modulo value
    MOD = 1000000
    
    # Initialize result
    result = 1
    
    # For each amino acid in the protein string, multiply the number of codon possibilities
    for amino_acid in protein_string:
        result = (result * codon_map[amino_acid]) % MOD
    
    # Multiply by 3 for the stop codon possibilities
    result = (result * 3) % MOD
    
    return result

# Read the protein string from the input file (provided as command-line argument)
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    protein_string = file.read().strip()

# Get the number of RNA strings modulo 1000000
result = count_rna_strings(protein_string)

# Output the result
print(result)

