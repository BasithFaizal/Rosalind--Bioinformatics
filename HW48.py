def scs(s, t):
    
    n, m = len(s), len(t)
    dp = [[""] * (m + 1) for _ in range(n + 1)]
    
    
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + s[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    
    lcs = dp[n][m]
    
    
    i = j = 0
    result = ""
    for c in lcs:
        while s[i] != c:
            result += s[i]
            i += 1
        while t[j] != c:
            result += t[j]
            j += 1
        result += c
        i += 1
        j += 1
    
   
    result += s[i:] + t[j:]
    return result


def main():
    import sys
    with open(sys.argv[1], 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    s = lines[0]
    t = lines[1]
    print(scs(s, t))

if __name__ == "__main__":
    main()
