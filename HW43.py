def nucleotide_probability(base, gc_content):
    if base in 'GC':
        return gc_content / 2
    else:
        return (1 - gc_content) / 2

def match_probability(s, gc_content):
    prob = 1.0
    for base in s:
        prob *= nucleotide_probability(base, gc_content)
    return prob

def compute_probability(N, x, s):
    p = match_probability(s, x)
    prob_none = (1 - p) ** N
    return 1 - prob_none

def main():
    import sys
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = f.read().strip().split()
        N = int(lines[0])
        x = float(lines[1])
        s = lines[2]
    result = compute_probability(N, x, s)
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()

