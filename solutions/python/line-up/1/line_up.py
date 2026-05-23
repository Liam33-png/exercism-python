def line_up(name, number):
    if str(number).endswith("1") and not str(number).endswith("11"):
        return f"{name}, you are the {number}st customer we serve today. Thank you!"
    if str(number).endswith("2") and not str(number).endswith("12"):
        return f"{name}, you are the {number}nd customer we serve today. Thank you!"
    if str(number).endswith("3") and not str(number).endswith("13"):
        return f"{name}, you are the {number}rd customer we serve today. Thank you!"
    else:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"

    