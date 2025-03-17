import sys

def parse_fasta(file_path):
    """Parse a FASTA file and return a dictionary of sequences with their IDs."""
    sequences = {}
    with open(file_path, 'r') as file:
        current_id = None
        current_seq = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]  # Remove '>' to get the ID
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            sequences[current_id] = ''.join(current_seq)
    return sequences

def gc_content(sequence):
    """Calculate the GC-content of a DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

# Read the input FASTA file
fasta_file = sys.argv[1]
sequences = parse_fasta(fasta_file)

# Calculate GC content for each sequence and find the highest
highest_gc_id = None
highest_gc_content = 0

for seq_id, seq in sequences.items():
    gc = gc_content(seq)
    if gc > highest_gc_content:
        highest_gc_content = gc
        highest_gc_id = seq_id

# Print the result
print(f"{highest_gc_id}\n{highest_gc_content:.6f}")
