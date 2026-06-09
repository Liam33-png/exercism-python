class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        self.checked = []

    def valid(self):
        self.checked = []
        self.card_num = self.card_num.replace(" ","")
        if len(self.card_num) <= 1:
            return False
        for number in self.card_num[-2::-2]:
            if not number.isdigit():
                return False
            elif int(number) * 2 <= 9:
               self.checked.append(int(number) * 2)
            else:
               self.checked.append(int(number) * 2 - 9 )
        for number in self.card_num[-1::-2]:
            if not number.isdigit():
                return False
        return (sum(self.checked) + sum(int(numba) for numba in self.card_num[-1::-2])) % 10 == 0
