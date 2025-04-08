import sys

MODULO = 1000000

def count_noncrossing_matchings(rna):
    n = len(rna)
    dp = [[0] * n for _ in range(n)]  # DP table
    
    # Base cases
    for i in range(n):
        dp[i][i] = 1  # Single nucleotide can't be matched
        if i + 1 < n:
            dp[i][i+1] = 1 if is_valid_pair(rna[i], rna[i+1]) else 0
    
    # Fill DP table
    for length in range(2, n, 2):  # Even lengths only
        for i in range(n - length):
            j = i + length
            total = 0
            for k in range(i + 1, j + 1, 2):  # Match pairs within the range
                if is_valid_pair(rna[i], rna[k]):
                    left = dp[i+1][k-1] if i+1 <= k-1 else 1
                    right = dp[k+1][j] if k+1 <= j else 1
                    total += left * right
                    total %= MODULO  # Modulo 1,000,000
            dp[i][j] = total
    
    return dp[0][n-1]

def is_valid_pair(a, b):
    """Check if two bases form a valid RNA bond (A-U, C-G)."""
    return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

if __name__ == "__main__":
    # Read input file
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        rna = "".join(line.strip() for line in file if not line.startswith(">"))  # Ignore FASTA header
    
    result = count_noncrossing_matchings(rna)
    print(result)
