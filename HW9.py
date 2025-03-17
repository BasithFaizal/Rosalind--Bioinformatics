import sys

def find_substring_locations(s, t):
    """
    Find all locations of the substring t in the string s.
    
    Parameters:
    s (str): The DNA string in which to search.
    t (str): The substring to locate in s.
    
    Returns:
    list: A list of 1-based starting positions of t in s.
    """
    locations = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            locations.append(i + 1)  # Convert to 1-based indexing
    return locations

# Read DNA strings from a file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    lines = file.read().strip().split()
    s = lines[0]  # First DNA string
    t = lines[1]  # Substring to locate

# Find and print all locations of t in s
locations = find_substring_locations(s, t)
print(" ".join(map(str, locations)))
