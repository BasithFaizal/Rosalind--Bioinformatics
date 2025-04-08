import sys

def read_fasta(file_path):
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    sequences = []
    current_seq = []
    
    for line in lines:
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    
    if current_seq:
        sequences.append("".join(current_seq))
    
    return sequences[0], sequences[1]  

def longest_common_subsequence(s, t):
    """Computes the LCS of two strings s and t using DP."""
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
   
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:  
            lcs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:  
            i -= 1
        else:  
            j -= 1
    
    return "".join(reversed(lcs)) 

if __name__ == "__main__":
    input_file = sys.argv[1]  
    s, t = read_fasta(input_file)
    lcs_result = longest_common_subsequence(s, t)
    
    print(lcs_result)  # Output LCS
