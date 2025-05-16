def parse_fasta(filename):
    with open(filename, 'r') as f:
        sequences = []
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def edit_distance(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,     # deletion
                dp[i][j - 1] + 1,     # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )
    return dp[n][m]

def main():
    import sys
    filename = sys.argv[1]
    s, t = parse_fasta(filename)
    print(edit_distance(s, t))

if __name__ == "__main__":
    main()
