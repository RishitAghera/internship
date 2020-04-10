class Luhn:
    card_num = 0

    def __init__(self, card_num):
        self.card_num = card_num[::-1].replace(" ", "")
        pass

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        if not self.card_num.isdigit():
            return False

        sum = 0
        for n in range(len(self.card_num)):
            print(self.card_num[n])
            if n % 2 != 0:
                temp = int(self.card_num[n]) * 2
                if temp > 9:
                    temp = temp - 9
                sum = sum + temp
            else:
                sum = sum + int(self.card_num[n])
        print(sum)
        if sum % 10 == 0:
            return True
        else:
            return False



