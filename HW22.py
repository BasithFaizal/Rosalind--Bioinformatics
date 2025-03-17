import sys

# Standard RNA codon table
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def read_fasta(filename):
    """ Reads a FASTA file and returns a dictionary {header: sequence}. """
    sequences = {}
    with open(filename, 'r') as file:
        current_label = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_label = line[1:]  # Remove '>'
                sequences[current_label] = ""
            else:
                sequences[current_label] += line
    return sequences

def transcribe(dna):
    """ Transcribes DNA to mRNA by replacing T with U. """
    return dna.replace("T", "U")

def translate(rna):
    """ Translates an RNA sequence into a protein sequence. """
    protein = ""
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == "Stop":
                break
            protein += amino_acid
    return protein

def remove_introns(dna, introns):
    """ Removes introns from the DNA sequence. """
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.fasta")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequences = read_fasta(fasta_file)

    # First sequence is the main DNA, the rest are introns
    dna_sequence = list(sequences.values())[0]
    introns = list(sequences.values())[1:]

    # Remove introns
    exon_sequence = remove_introns(dna_sequence, introns)

    # Transcribe and translate
    rna_sequence = transcribe(exon_sequence)
    protein_sequence = translate(rna_sequence)

    print(protein_sequence)

if __name__ == "__main__":
    main()
