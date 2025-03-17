import sys

def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return ''.join(line.strip() for line in lines[1:])  # Skip the header

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def find_reverse_palindromes(dna):
    results = []
    n = len(dna)
    
    for length in range(4, 13):  # Lengths between 4 and 12
        for i in range(n - length + 1):
            sub_seq = dna[i:i+length]
            if sub_seq == reverse_complement(sub_seq):
                results.append((i + 1, length))  # 1-based index
    
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <fasta_file>")
        return
    
    fasta_file = sys.argv[1]
    dna_sequence = read_fasta(fasta_file)
    results = find_reverse_palindromes(dna_sequence)
    
    for pos, length in results:
        print(pos, length)

if __name__ == "__main__":
    main()
