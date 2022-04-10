class BigBell():
    def __init__(self):
        self.bell = 0
    
    def sound(self):
        if self.bell % 2 == 0:
            print('ding')
        else:
            print('dong')
        self.bell += 1
