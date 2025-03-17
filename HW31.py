import sys

def read_fasta(filename):
    """Reads a FASTA file and returns a list of sequences."""
    with open(filename, 'r') as file:
        sequences = {}
        current_label = None
        current_sequence = []
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_label:
                    sequences[current_label] = "".join(current_sequence)
                current_label = line[1:]  # Remove '>'
                current_sequence = []
            else:
                current_sequence.append(line)
        
        if current_label:
            sequences[current_label] = "".join(current_sequence)
    
    return list(sequences.values())  # Return the sequences as a list

def transition_transversion_ratio(s1, s2):
    """Computes the transition/transversion ratio between s1 and s2."""
    transitions = 0
    transversions = 0

    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1 in purines and base2 in purines) or (base1 in pyrimidines and base2 in pyrimidines):
                transitions += 1
            else:
                transversions += 1
    
    return transitions / transversions if transversions > 0 else float('inf')

if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    sequences = read_fasta(input_file)

    s1 = sequences[0]
    s2 = sequences[1]

    ratio = transition_transversion_ratio(s1, s2)
    
    print(f"{ratio:.6f}")
