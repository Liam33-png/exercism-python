"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    return " :: ".join(map(lambda word : f"{vocab_words[0]}{word}" if word != vocab_words[0] else word, vocab_words))


def remove_suffix_ness(word):
    if word.removesuffix("ness").endswith("i"):
        return word.removesuffix("iness") + "y"
    else:
        return word.removesuffix("ness")



def adjective_to_verb(sentence, index):
    words = list(sentence.split(" "))
    return f"{words[index].replace(".","")}en"
