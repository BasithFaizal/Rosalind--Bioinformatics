import sys

def factorial(n):
    """Computes factorial of n manually (n!)"""
    result = 1
    for i in range(2, n + 1):  # Multiply from 2 to n
        result *= i
    return result

def count_perfect_matchings(rna_string):
    """Computes the total number of perfect matchings"""
    count_A = rna_string.count('A')
    count_C = rna_string.count('C')
    
    # Compute factorials manually
    return factorial(count_A) * factorial(count_C)

def read_fasta(file_path):
    """Reads RNA sequence from FASTA file"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    rna_string = "".join(line.strip() for line in lines if not line.startswith(">"))
    return rna_string

# Main execution
if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    rna_sequence = read_fasta(input_file)
    result = count_perfect_matchings(rna_sequence)
    print(result)
