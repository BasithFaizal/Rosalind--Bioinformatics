import sys
from math import comb

def probability_at_least_N(k, N):
    """
    Computes the probability that at least N Aa Bb organisms will be in the k-th generation.
    
    Parameters:
    k (int): The generation number.
    N (int): The minimum number of Aa Bb organisms required.
    
    Returns:
    float: The probability that at least N Aa Bb organisms are in the k-th generation.
    """
    # Total number of offspring in the k-th generation is 2^k
    total_offspring = 2 ** k
    probability_Aa_Bb = 1 / 4  # Probability of Aa Bb genotype for each offspring
    probability_not_Aa_Bb = 3 / 4  # Probability of not Aa Bb
    
    # Calculate the cumulative probability for at least N Aa Bb organisms
    probability_at_least_N = 0
    for i in range(N, total_offspring + 1):
        probability_at_least_N += comb(total_offspring, i) * (probability_Aa_Bb ** i) * (probability_not_Aa_Bb ** (total_offspring - i))
    
    return probability_at_least_N

# Read input from file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    k, N = map(int, file.read().split())

# Compute the probability
result = probability_at_least_N(k, N)

# Print the result
print(f"{result:.6f}")

