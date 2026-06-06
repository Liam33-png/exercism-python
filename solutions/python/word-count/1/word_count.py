alphabet = tuple("abcdefghijklmnopqrstuvwxyz'1234567890")
def count_words(sentence):
    output = {}
    string = ""
    for word in sentence:
        if word.lower() in alphabet:
            string += word.lower()
        elif not string == "":
            string = string.strip("'")
            if string not in output:
                output[string] = 1
            else:
                output[string] += 1
            string = ""
    string = string.strip("'")
    if not string == "":
        if string not in output:
            output[string] = 1
        else:
            output[string] += 1
    return output