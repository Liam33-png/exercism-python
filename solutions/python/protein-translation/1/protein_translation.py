codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}
def proteins(strand):
    groups = []
    for i in range(len(strand) // 3):
        print(i)
        groups.append(strand[3 * i:3 + (3 * i)])
    protein = [codon_table.get(trio) for trio in groups]
    if "STOP" in protein:
        return protein[:protein.index("STOP")] 
    return protein