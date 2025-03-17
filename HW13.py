import sys

def expected_dominant_offspring(couples):
    """
    Computes the expected number of offspring displaying the dominant phenotype.
    
    Parameters:
    couples (list): A list of six integers representing the number of couples with specific genotype pairings.
    
    Returns:
    float: The expected number of dominant offspring.
    """
    # Probability of dominant phenotype in offspring for each genotype pairing
    probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    
    # Compute the expected number of dominant offspring
    expected_offspring = 2 * sum(couples[i] * probabilities[i] for i in range(6))
    
    return expected_offspring

# Read input from file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    couples = list(map(int, file.read().strip().split()))

# Compute and print the expected number of dominant offspring
print(expected_dominant_offspring(couples))
