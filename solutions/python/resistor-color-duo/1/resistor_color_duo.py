colours = { 
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
def value(colors):
    values = []
    for color in colors:
        if len(values) < 2:
            values.append(str(colours.get(color)))
    return int("".join((values)))
print(value(["green", "brown", "orange"]))