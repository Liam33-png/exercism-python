def to_rna(dna_strand):
    rna = []
    for dna in dna_strand:
        if dna == "G":
            rna.append("C")
        elif dna == "C":
            rna.append("G")
        elif dna == "T":
            rna.append("A")
        elif dna == "A":
            rna.append("U")
    return "".join(rna)

