class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        res = 0
        for i in range(1, n + 1):
            res += self.transform(i)
        return res


class PowerSummator(Summator):
    def __init__(self, b) -> None:
        self.power = b

    def transform(self, n):
        return super().transform(n) ** self.power


class SquareSummator(PowerSummator):
    def __init__(self) -> None:
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self) -> None:
        super().__init__(3)
