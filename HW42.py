def parse_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as f:
        current = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current:
                    sequences.append(current)
                    current = ''
            else:
                current += line
        if current:
            sequences.append(current)
    return sequences

def compute_p_distance(s1, s2):
    mismatches = sum(1 for a, b in zip(s1, s2) if a != b)
    return mismatches / len(s1)

def build_distance_matrix(sequences):
    n = len(sequences)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            dist = compute_p_distance(sequences[i], sequences[j])
            row.append(round(dist, 5))  
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{val:.5f}" for val in row))

def main():
    import sys
    file_path = sys.argv[1]
    sequences = parse_fasta(file_path)
    matrix = build_distance_matrix(sequences)
    print_matrix(matrix)

if __name__ == "__main__":
    main()
