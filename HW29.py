import sys

def generate_permutations(arr, l, r, results):
    """Generate all permutations of the given array"""
    if l == r:
        results.append(arr[:])  # Append a copy of the current permutation
    else:
        for i in range(l, r):
            arr[l], arr[i] = arr[i], arr[l]  # Swap
            generate_permutations(arr, l + 1, r, results)
            arr[l], arr[i] = arr[i], arr[l]  # Backtrack

def generate_signed_permutations(n):
    """Generate all signed permutations of length n"""
    base_perms = []
    generate_permutations(list(range(1, n + 1)), 0, n, base_perms)
    
    signed_perms = []
    for perm in base_perms:
        for mask in range(1 << n):  # 2^n possibilities
            signed_perm = [(perm[i] if (mask & (1 << i)) == 0 else -perm[i]) for i in range(n)]
            signed_perms.append(signed_perm)
    
    return signed_perms

# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return int(file.readline().strip())

if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    n = read_input(input_file)
    
    signed_permutations = generate_signed_permutations(n)
    
    print(len(signed_permutations))  # Print the total count
    for perm in signed_permutations:
        print(" ".join(map(str, perm)))  # Print each permutation
