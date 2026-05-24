def sum_of_multiples(limit, multiples):
    sum = []
    total = 0
    for i in range (limit):
        for multiple in multiples:
            if multiple != 0 and i % multiple == 0 and i not in sum:
                sum.append(i)
    for number in sum:
        total += number
    return total