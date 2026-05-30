def decode(string):
    decoded = []
    multi = ""
    numbers ="1234567890"
    
    for character in string:
        if character in numbers:
            multi += character
        else:
            try:
                decoded.append(int(multi) * character)
            except ValueError:
                decoded.append(character)
            multi = ""
    return "".join(decoded)




def encode(string):
    encoded = []
    last = ""
    counter = 1
    for word in string:
        if word == last:
            counter += 1
        else:
            if counter != 1:
                encoded.append(str(counter) + last)
            else:
                if last != "":
                    encoded.append(str(last))
            counter = 1
        last = word
    if string:
        if counter != 1:
            encoded.append(str(counter) + word)
        else:
            encoded.append(word)

    return "".join(encoded)  
