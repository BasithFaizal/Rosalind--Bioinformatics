# Monoisotopic mass table for amino acids
amino_acid_mass = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
    'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
    'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
    'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
}

def calculate_protein_weight(protein_string):
    total_weight = 0
    for aa in protein_string:
        total_weight += amino_acid_mass.get(aa, 0)  # Add the mass of the amino acid, defaulting to 0 if not found
    return total_weight

# Main function to read input from file and calculate total weight
import sys

# Read protein string from file
with open(sys.argv[1], 'r') as file:
    protein_string = file.read().strip()  # Read protein string from the file

# Calculate total weight of the protein
total_weight = calculate_protein_weight(protein_string)

# Output the total weight
print(f"{total_weight:.6f}")
