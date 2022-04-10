from functools import lru_cache


class Selector:
    def __init__(self, lst):
        self.lst = lst[:]
        self.evens = []
        self.odds = []
    
    @lru_cache
    def evens_odds(self):
        for i in self.lst:
            if i % 2 != 0:
                self.odds.append(i)
            else:
                self.evens.append(i)

    def get_odds(self):
        self.evens_odds()
        return self.odds

    def get_evens(self):
        self.evens_odds()
        return self.evens


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
