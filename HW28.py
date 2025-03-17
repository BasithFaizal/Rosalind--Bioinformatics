import sys

def compute_log_probability(dna, gc_contents):
    """Computes log10 probability for each GC-content in the list"""
    count_GC = sum(1 for base in dna if base in "GC")
    count_AT = len(dna) - count_GC  # Remaining are A or T
    
    log_probs = []
    for gc in gc_contents:
        p_GC = gc / 2
        p_AT = (1 - gc) / 2
        log_prob = (count_GC * log10(p_GC)) + (count_AT * log10(p_AT))
        log_probs.append(round(log_prob, 3))  # Round for precision
    
    return log_probs

def log10(x):
    """Computes log10(x) without using math module"""
    from math import log
    return log(x) / log(10)

# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        dna = file.readline().strip()
        gc_contents = list(map(float, file.readline().strip().split()))
    return dna, gc_contents

if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    dna, gc_contents = read_input(input_file)
    result = compute_log_probability(dna, gc_contents)
    print(" ".join(map(str, result)))  # Print results space-separated
