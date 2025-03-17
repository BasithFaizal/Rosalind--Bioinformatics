def generate_permutations(n):
    """
    Function to generate all permutations of numbers from 1 to n using recursion.
    """
    # Helper function for backtracking
    def backtrack(current, remaining, all_permutations):
        if not remaining:  # When no elements are remaining to be placed
            all_permutations.append(current)  # Add the current permutation to the list
            return
        for i in range(len(remaining)):
            backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:], all_permutations)

    all_permutations = []
    backtrack([], list(range(1, n+1)), all_permutations)
    return all_permutations

# Main function to read input from a file
import sys

# Read input from file
with open(sys.argv[1], 'r') as file:
    n = int(file.read().strip())  # Read the integer n from the input file

# Generate all permutations of length n
permutations = generate_permutations(n)

# Output the number of permutations followed by the list of permutations
print(len(permutations))
for perm in permutations:
    print(" ".join(map(str, perm)))
