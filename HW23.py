import sys

def generate_strings(alphabet, n, current_string, results):
    """ Recursively generate all strings of length n from the given alphabet. """
    if len(current_string) == n:
        results.append(current_string)
        return
    
    for char in alphabet:
        generate_strings(alphabet, n, current_string + char, results)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)

    # Read input file
    with open(sys.argv[1], 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Parse alphabet and n
    alphabet = lines[0].split()  # Ordered alphabet
    n = int(lines[1])  # Length of strings to generate

    # Generate strings
    results = []
    generate_strings(alphabet, n, "", results)

    # Print results in lexicographic order
    print("\n".join(results))

if __name__ == "__main__":
    main()
