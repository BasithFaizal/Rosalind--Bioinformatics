import sys

def dominant_allele_probability(k, m, n):
    """
    Calculate the probability of producing an offspring with a dominant allele.
    
    Parameters:
    k (int): Number of homozygous dominant organisms.
    m (int): Number of heterozygous organisms.
    n (int): Number of homozygous recessive organisms.
    
    Returns:
    float: Probability of producing an offspring with a dominant allele.
    """
    total = k + m + n  # Total population
    
    # Probabilities of specific pairings:
    # Homozygous dominant (k) can pair with:
    prob_kk = (k / total) * ((k - 1) / (total - 1))  # Two homozygous dominant
    prob_km = (k / total) * (m / (total - 1)) * 2   # Homozygous dominant & heterozygous
    prob_kn = (k / total) * (n / (total - 1)) * 2   # Homozygous dominant & homozygous recessive
    
    # Heterozygous (m) can pair with:
    prob_mm = (m / total) * ((m - 1) / (total - 1))  # Two heterozygous
    prob_mn = (m / total) * (n / (total - 1)) * 2    # Heterozygous & homozygous recessive
    
    # Probability of offspring with a dominant allele:
    prob_dominant = (
        prob_kk * 1.0 +          # All offspring are dominant
        prob_km * 1.0 +          # All offspring are dominant
        prob_kn * 1.0 +          # All offspring are dominant
        prob_mm * 0.75 +         # 75% of offspring are dominant
        prob_mn * 0.5            # 50% of offspring are dominant
    )
    
    return prob_dominant

# Read input from a file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    k, m, n = map(int, file.read().strip().split())

# Calculate and print the probability
print(f"{dominant_allele_probability(k, m, n):.5f}")
