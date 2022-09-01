from datetime import datetime as dt


def very_lucky(time: str):
    sum_h, sum_m = map(lambda x: sum(map(int, list(x))), time.split(":"))
    if sum_h != sum_m:
        return True
    return False


lhours = tuple(int(i) for i in input().split())
lminutes = tuple(int(i) for i in input().split())

lucky_time = [
    t for hours in lhours
    for minutes in lminutes
    if very_lucky(t := f"{hours:02d}:{minutes:02d}")
]

print(*sorted(lucky_time, key=lambda x: dt.strptime(x, "%H:%M")), sep="\n")
