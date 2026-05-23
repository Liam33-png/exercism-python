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
def label(colors):
    values = []
    counter = 0
    for color in colors:
        if len(values) < 2:
            values.append(str(colours.get(color)))
    if len(colors) >= 3:
        translated = int(f'{int("".join((values)))}{int(colours.get(colors[2])) * "0"}')
    if translated < 10**3:
        translated = f'{str(translated).removesuffix("")} ohms'
    elif 10**6 > translated >= 10**3:
        translated = f'{str(translated).removesuffix("000")} kiloohms'
    elif 10**9 > translated >= 10**6:
        translated = f'{str(translated).removesuffix("000000")} megaohms'
    elif 10**12 > translated >= 10**9:
        translated = f'{str(translated).removesuffix("000000000")} gigaohms'
    return translated