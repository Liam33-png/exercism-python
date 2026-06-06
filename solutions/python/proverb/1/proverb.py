
def proverb(*input, qualifier=None):
    output = []
    for i in range(len(input)):
        if i + 1 < len(input):
            output.append(f"For want of a {input[i]} the {input[i + 1]} was lost.")
    if input:
        if qualifier:
            output.append(f"And all for the want of a {qualifier} {input[0]}.")
        else:
            output.append(f"And all for the want of a {input[0]}.")
    return output