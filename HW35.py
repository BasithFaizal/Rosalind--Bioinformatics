import sys

def count_internal_nodes(file_path):
    """Reads an integer n from the file and calculates the number of internal nodes."""
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
    
    # Compute internal nodes using the formula
    internal_nodes = n - 2
    print(internal_nodes)

if __name__ == "__main__":
    input_file = sys.argv[1]  
    count_internal_nodes(input_file)
