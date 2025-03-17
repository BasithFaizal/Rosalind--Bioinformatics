import sys

# Genetic code dictionary
GENETIC_CODE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_rna_to_protein(rna):
    """
    Translate an RNA string into a protein string.
    
    Parameters:
    rna (str): An RNA string.
    
    Returns:
    str: The protein string encoded by the RNA.
    """
    protein = []
    for i in range(0, len(rna), 3):  # Read RNA in codons of 3 nucleotides
        codon = rna[i:i+3]
        if len(codon) < 3:
            break  # Ignore incomplete codons at the end
        amino_acid = GENETIC_CODE.get(codon, '')
        if amino_acid == 'Stop':
            break  # Stop translation at stop codons
        protein.append(amino_acid)
    return ''.join(protein)

# Read RNA string from a file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    rna = file.read().strip()

# Translate and print the protein string
print(translate_rna_to_protein(rna))
