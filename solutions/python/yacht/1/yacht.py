# Score categories.
# Change the values as you see fit.
from unicodedata import category

YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    dice_rolls = {}
    points = 0
    for roll in dice:
        dice_rolls[roll] = dice_rolls.get(roll,0) + 1
    if category == ONES:
        points = dice_rolls.get(1,0)
    elif category == TWOS:
        points = dice_rolls.get(2,0) * 2
    elif category == THREES:
        points = dice_rolls.get(3,0) * 3
    elif category == FOURS:
        points = dice_rolls.get(4,0) * 4
    elif category == FIVES:
        points = dice_rolls.get(5,0) * 5
    elif category == SIXES:
        points = dice_rolls.get(6,0) * 6
    elif category == FULL_HOUSE:
        if sorted(dice_rolls.values()) == [2,3]:
           points = sum([x * dice_rolls.get(x) for x in dice_rolls.keys()])
    elif category == FOUR_OF_A_KIND:
            points = sum([x * 4 for x in dice_rolls.keys() if dice_rolls.get(x) >= 4])
    elif category == LITTLE_STRAIGHT:
        if sorted(dice_rolls.keys()) == [1,2,3,4,5]:
            points = 30
    elif category == BIG_STRAIGHT:
        if sorted(dice_rolls.keys()) == [2,3,4,5,6]:
            points = 30
    elif category == CHOICE:
        points = sum(dice)
    elif category == YACHT:
        if sorted(dice_rolls.values()) == [5]:
            points = 50
    return points