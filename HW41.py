def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().splitlines()
    alphabet = lines[0].split()
    n = int(lines[1])
    return alphabet, n

def generate_kmers(alphabet, max_len):
    result = []

    def build(current):
        if 1 <= len(current) <= max_len:
            result.append(current)
        if len(current) == max_len:
            return
        for ch in alphabet:
            build(current + ch)

    build("")  
    return result

def main():
    import sys
    file_path = sys.argv[1]
    alphabet, n = read_input(file_path)
    kmers = generate_kmers(alphabet, n)
    for kmer in kmers:
        print(kmer)

if __name__ == "__main__":
    main()
