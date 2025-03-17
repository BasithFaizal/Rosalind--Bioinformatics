import sys

def read_graph(filename):
    """Reads a graph from an adjacency list in a file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())  # Number of nodes
    edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    
    return n, edges

def find_connected_components(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    
    visited = set()
    components = 0

    def dfs(node):
      
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                stack.extend(graph[curr])
    
    for node in range(1, n + 1):
        if node not in visited:
            dfs(node)
            components += 1  
    
    return components

if __name__ == "__main__":
    input_file = sys.argv[1] 
    n, edges = read_graph(input_file)
    
    num_components = find_connected_components(n, edges)
    
    print(num_components - 1)
