monoisotopic_mass = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def find_amino_acid_by_mass(diff, tolerance=0.01):
    for aa, mass in monoisotopic_mass.items():
        if abs(mass - diff) <= tolerance:
            return aa
    return None  
def reconstruct_protein(prefix_masses):
    protein = ""
    for i in range(1, len(prefix_masses)):
        diff = prefix_masses[i] - prefix_masses[i - 1]
        aa = find_amino_acid_by_mass(diff)
        if aa:
            protein += aa
        else:
            raise ValueError(f"No matching amino acid found for mass difference: {diff}")
    return protein


def main():
    import sys
    with open(sys.argv[1], 'r') as f:
        masses = [float(line.strip()) for line in f if line.strip()]
    protein = reconstruct_protein(masses)
    print(protein)

if __name__ == "__main__":
    main()
