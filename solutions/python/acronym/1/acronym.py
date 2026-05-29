def abbreviate(words):
    
    words = words.replace(" ","-").replace("_","").split("-")
    abbreviation = [word[0] if word else "" for word in words]
    return "".join(abbreviation).upper()