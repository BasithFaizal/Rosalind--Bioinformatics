import sys

def read_fasta(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()
    
    dna_string = "".join(line.strip() for line in lines if not line.startswith(">"))
    return dna_string

def compute_failure_array(s):

    n = len(s)
    failure = [0] * n  
    j = 0  
    
    for i in range(1, n):
        while (j > 0 and s[i] != s[j]):
            j = failure[j - 1] 
        
        if s[i] == s[j]: 
            j += 1
            failure[i] = j
        else:
            failure[i] = 0
    
    return failure

if __name__ == "__main__":
    input_file = sys.argv[1]  
    dna_string = read_fasta(input_file)
    failure_array = compute_failure_array(dna_string)
    
    print(" ".join(map(str, failure_array))) 
