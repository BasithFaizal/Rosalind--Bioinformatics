import sys

def factorial_mod(n, k, mod=1000000):
    """Computes P(n, k) = n! / (n-k)! modulo mod"""
    result = 1
    for i in range(n, n - k, -1):  # Compute product from n to (n-k+1)
        result = (result * i) % mod
    return result

# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        n, k = map(int, file.readline().strip().split())
    return n, k

if __name__ == "__main__":
    input_file = sys.argv[1]  # Read input file from command line
    n, k = read_input(input_file)
    print(factorial_mod(n, k))
