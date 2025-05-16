import sys

MOD = 1000000

def binomial_sum(n, m):

    C = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        C[i][0] = 1
        for k in range(1, i + 1):
            C[i][k] = (C[i-1][k-1] + C[i-1][k]) % MOD

    return sum(C[n][k] for k in range(m, n + 1)) % MOD

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        return

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().strip().split())

    print(binomial_sum(n, m))

if __name__ == "__main__":
    main()



