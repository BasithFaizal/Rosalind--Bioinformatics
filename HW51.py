def build_trie(patterns):
    trie = {1: {}}  # Start with root node 1
    next_node = 2   # Next available node label
    edges = []      # To store (parent, child, symbol)

    for pattern in patterns:
        current_node = 1
        for char in pattern:
            if char in trie[current_node]:
                current_node = trie[current_node][char]
            else:
                trie[current_node][char] = next_node
                trie[next_node] = {}
                edges.append((current_node, next_node, char))
                current_node = next_node
                next_node += 1
    return edges

def main():
    import sys
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        patterns = [line.strip() for line in f if line.strip()]
    
    edges = build_trie(patterns)
    
    for parent, child, symbol in edges:
        print(f"{parent} {child} {symbol}")

if __name__ == "__main__":
    main()
