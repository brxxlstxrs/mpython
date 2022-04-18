class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        res = 0
        for i in range(1, n + 1):
            res += self.transform(i)


class SquareSummator(Summator):
    def transform(self, n):
        return super().transform(n) ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return super().transform(n) ** 3

