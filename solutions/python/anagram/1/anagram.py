def find_anagrams(word, candidates):
    solution = []
    for candidate in candidates:
        if sorted(list(candidate.lower())) == sorted(list(word.lower())) and word.lower() != candidate.lower():
            solution.append(candidate)
    return solution
