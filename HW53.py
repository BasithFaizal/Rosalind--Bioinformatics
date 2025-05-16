def expected_substrings(n, s, A):
    result = []
    k = len(s)
    
    for gc_content in A:
        prob = 1.0
        for base in s:
            if base in 'GC':
                prob *= gc_content / 2
            else:
                prob *= (1 - gc_content) / 2
        
        expected = prob * (n - k + 1)
        result.append(expected)
    
    return result

def main():
    import sys
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        s = f.readline().strip()
        A = list(map(float, f.readline().strip().split()))
    
    B = expected_substrings(n, s, A)
    
    for b in B:
        print(f"{b:.3f}")

if __name__ == "__main__":
    main()
