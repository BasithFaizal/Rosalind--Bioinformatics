import sys

def hamming_distance(s, t):
    """
    Calculate the Hamming distance between two DNA strings s and t.

    Parameters:
    s (str): First DNA string.
    t (str): Second DNA string.

    Returns:
    int: The Hamming distance between s and t.
    """
    # Ensure the strings are of equal length
    assert len(s) == len(t), "DNA strings must be of equal length"
    
    # Count mismatches between the strings
    return sum(1 for a, b in zip(s, t) if a != b)

# Read input from a file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    lines = file.read().strip().split()
    s = lines[0]
    t = lines[1]

# Calculate and print the Hamming distance
print(hamming_distance(s, t))
