"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number for number in range(number, number + 3)]


def concatenate_rounds(rounds_1, rounds_2):
    rounds_1.extend(rounds_2)
    return rounds_1

def list_contains_round(rounds, number):
    return number in rounds
def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    return (hand[0] + hand[len(hand) - 1]) / 2 == card_average(hand) or hand[int((len(hand) + 1 )/ 2 - 1)]  == card_average(hand)

def average_even_is_average_odd(hand):
    return sum(hand[::2]) / len(hand[::2]) == sum(hand[1::2]) / len(hand[1::2])

def maybe_double_last(hand):
    return list(map(lambda card: card * 2 if hand[len(hand) - 1] == 11 and card is hand[len(hand) - 1]else card, hand))

