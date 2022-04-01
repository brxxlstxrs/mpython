class Balance:
    def __init__(self):
        self.r = 0
        self.l = 0
    
    def add_right(self, n):
        self.r += n

    def add_left(self, n):
        self.l += n

    def result(self):
        if self.r > self.l:
            return 'R'
        elif self.l > self.r:
            return 'L'
        else:
            return '='
