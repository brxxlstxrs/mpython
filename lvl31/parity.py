class OddEvenSeparator:
    def __init__(self):
        self.odd = []
        self.even =[]

    def add_number(self, n):
        if n % 2 == 0:
            self.odd.append(n)
        else:
            self.even.append(n)

        
