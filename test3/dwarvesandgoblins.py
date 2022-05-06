import sys


def print_creatures(creatures: list[str]) -> None:
    print(': '.join(creatures))


def select_goblins(s: str) -> list[str]:
    numbers = s.split()
    goblins = []
    for n in numbers:
        if int(n) % 3 == 0:
            goblins.append(n)

    return goblins


def select_dwarves(s: str) -> list[str]:
    numbers = s.split()
    dwarves = []
    for n in numbers:
        if len(n) <= 2:
            dwarves.append(n)

    return dwarves


def main() -> None:
    for i, line in enumerate(sys.stdin, 1):
        if i % 2 != 0:
            creatures = select_goblins(line)
        else:
            creatures = select_dwarves(line)
        print_creatures(creatures)


if __name__ == '__main__':
    main()

