alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rows(letter):
    triangle = []
    if letter == "A":
        return ["A"]
    else:
        for character in alphabet[:alphabet.index(letter.upper()) + 1]:
            if character == "A":
                triangle.append(" " * (alphabet.index(letter) - alphabet.index(character)) + character + " " * (2 * alphabet.index(character) + 2 - 3)   +" " * (alphabet.index(letter) - alphabet.index(character)))
            else:
                triangle.append(" " * (alphabet.index(letter) - alphabet.index(character)) + character + " " * (2 * alphabet.index(character) + 2 - 3) + character  +" " * (alphabet.index(letter) - alphabet.index(character)))
        for character in alphabet[alphabet.index(letter.upper()) - 1::-1]:
            if character == "A":
                triangle.append(" " * (alphabet.index(letter) - alphabet.index(character)) + character + " " * (2 * alphabet.index(character) + 2 - 3)   +" " * (alphabet.index(letter) - alphabet.index(character)))
            else:
                triangle.append(" " * (alphabet.index(letter) - alphabet.index(character)) + character + " " * (2 * alphabet.index(character) + 2 - 3) + character  +" " * (alphabet.index(letter) - alphabet.index(character)))
    return triangle