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

def find_subsequence_indices(s, t):
    """Finds the 1-based indices of s where t appears as a subsequence."""
    indices = []
    t_index = 0  # Pointer for t
    
    for i in range(len(s)):
        if t_index < len(t) and s[i] == t[t_index]:
            indices.append(i + 1)  # Convert 0-based index to 1-based
            t_index += 1
        if t_index == len(t):  # Stop early if we matched all of t
            break

    return indices

if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    sequences = read_fasta(input_file)

    s = sequences[0]
    t = sequences[1]

    indices = find_subsequence_indices(s, t)
    
    print(" ".join(map(str, indices)))

