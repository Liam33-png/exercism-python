face_cards = ("J","Q","K")


def value_of_card(card):
    if str(card).upper() in face_cards:
        return 10
    elif str(card).upper() == "A":
        return 1
    elif int(card) in range(2,11):
        return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two



def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    return (card_one == "A" and value_of_card(card_two) == 10) or value_of_card(card_one) == 10 and card_two == "A"
        


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return value_of_card(card_one) + value_of_card(card_two) in range(9,12)
