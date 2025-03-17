import sys

def rabbit_pairs(n, k):
    """
    Calculate the total number of rabbit pairs after n months with k pairs produced per generation.
    
    Parameters:
    n (int): Number of months.
    k (int): Number of rabbit pairs produced per generation.
    
    Returns:
    int: Total number of rabbit pairs after n months.
    """
    if n == 1:
        return 1  # Base case: At month 1, there is 1 pair of rabbits
    elif n == 2:
        return 1  # Base case: At month 2, there is still 1 pair of rabbits

    # Use a bottom-up approach to calculate the sequence
    prev = 1  # F(n-1)
    curr = 1  # F(n-2)
    
    for _ in range(3, n + 1):
        next_rabbits = curr + k * prev  # F(n) = F(n-1) + k * F(n-2)
        prev, curr = curr, next_rabbits
    
    return curr

# Read input from a file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    data = file.read().strip()
    n, k = map(int, data.split())  # Parse n and k from the input file

# Calculate and print the result
print(rabbit_pairs(n, k))
