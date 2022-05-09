def words(num_of_words: int, lst: tuple[str]) -> str | None:
    res = []
    for s in lst:
        if len(s.split()) == num_of_words:
            res.append(s)
    return max(res) if res else None


def no_sub(substr: str, lst: tuple[str]) -> str | None:
    res = []
    for s in lst:
        if substr.lower() not in s.lower():
            res.append(s)
    return max(res) if res else None


def ends(value: int, lst: tuple[str]) -> str | None:
    res = []
    function = lambda x: x[-1].isalpha()
    if value != 0:
        function = lambda x: not(x[-1].isalpha())

    for s in lst:
        res.append(s) if function(s) else 0
    return max(res) if res else None
        

def warning(*messages, **params) -> dict[str, str]:
    dct = {}
    if 'words' in params.keys():
        dct['words'] = words(params['words'], messages)
    if 'no_sub' in params.keys():
        dct['no_sub'] = no_sub(params['no_sub'], messages)
    if 'ends' in params.keys():
        dct['ends'] = ends(params['ends'], messages)

    return {k: v for k, v in dct.items() if v is not None}


messages = [
    "And let them remove", "the spell from this",
    "fallen broomstick", "so that it flies",
    "like new!"
]
params = {
    "words": 5,
    "ends": 0
}
print(warning(*messages, **params))
