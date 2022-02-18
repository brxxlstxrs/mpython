from collections import Counter

places = ("Gloomy",)

data = ["It", "Boring",
"Eve", "Crop"]


def step_by_boss(*args, letters=3):
    global places
    res = list(places)
    for e in args:
        if e not in places:
            print(Counter(e.lower()))
            if len([i for i in Counter(e).values() if i == 1]) >= letters:
                res.append(e)
    places = tuple(res)


step_by_boss(*data, letters=4)
print(places)
