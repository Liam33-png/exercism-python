def is_valid(isbn):
    isbn = list(isbn.replace("-",""))
    if len(isbn) != 10:
        return False
    for character in isbn:
        if (character not in "1234567890X") or (character == "X" and "X" not in isbn[9]):
            return False
    if isbn[9] == "X":
        isbn[9] = "10"
    return (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + int(isbn[9]) * 1) % 11 == 0
