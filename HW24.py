import sys

def longest_subsequence(arr, increasing=True):
    """ Finds the longest increasing or decreasing subsequence using DP + backtracking. """
    n = len(arr)
    dp = [1] * n  # Length of longest subsequence ending at index i
    prev = [-1] * n  # To reconstruct the sequence

    for i in range(n):
        for j in range(i):
            if (increasing and arr[j] < arr[i]) or (not increasing and arr[j] > arr[i]):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    # Find the index of the maximum value in dp
    max_index = max(range(n), key=lambda i: dp[i])

    # Reconstruct the sequence
    sequence = []
    while max_index != -1:
        sequence.append(arr[max_index])
        max_index = prev[max_index]

    return sequence[::-1]  # Reverse to get correct order

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)

    # Read input file
    with open(sys.argv[1], 'r') as file:
        lines = file.read().strip().split("\n")

    # Parse n and the permutation
    n = int(lines[0])  # Length of permutation
    permutation = list(map(int, lines[1].split()))  # Convert to list of integers

    # Find LIS and LDS
    lis = longest_subsequence(permutation, increasing=True)
    lds = longest_subsequence(permutation, increasing=False)

    # Print results
    print(" ".join(map(str, lis)))
    print(" ".join(map(str, lds)))

if __name__ == "__main__":
    main()
