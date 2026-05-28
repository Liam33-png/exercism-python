alphabet = "abcdefghijklmnopqrstuvwxyz"
def encode(plain_text):
    output = ""
    group_of_5 = ""
    encoded = []
    for character in plain_text.strip().replace(" ",""):
        character = character.lower()
        if character in alphabet:
            character = alphabet[25 - alphabet.index(character)]
            group_of_5 += character.lower()
        elif not character in ".,?" :
            group_of_5 += character
        if len(group_of_5) == 5:
            encoded.append(group_of_5)
            group_of_5 = ""
    encoded.append(group_of_5)
    return " ".join(encoded).strip()
        
def decode(ciphered_text):
    decoded = []
    for character in ciphered_text.replace(" ","").strip():
        if character in alphabet:
            character = alphabet[25 - alphabet.index(character)]
            decoded.append(character)
        else:
            decoded.append(character)
    return "".join(decoded)