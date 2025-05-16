def total_subsets_mod(n, mod=1_000_000):
    return pow(2, n, mod)

def main():
    import sys
    file = sys.argv[1]
    with open(file, 'r') as f:
        n = int(f.read().strip())
    result = total_subsets_mod(n)
    print(result)

if __name__ == "__main__":
    main()
