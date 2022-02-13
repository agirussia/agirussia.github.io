# https://github.com/agirussia/agirussia.github.io/blob/main/challenges/miniagi1/animals1.pdf
# https://trinket.io/python/1b3e856cc7
# https://trinket.io/python/28569b8bb8
# https://t.me/practical_agi_russian/1848

from collections import defaultdict

tuples = [
    ('pm', 'do'),
    ('pm', 'wo'),
    ('pm', 'pe'),
    ('pm', 'wi'),
    ('fm', 'ti'),
    ('fm', 'ca'),
    ('fm', 'pe'),
    ('fm', 'wi'),
    ('ta', 'do'),
    ('ta', 'pe'),
    ('td', 'wo'),
    ('td', 'wi'),
    ('la', 'ti'),
    ('la', 'wi'),
    ('sm', 'ca'),
    ('sm', 'pe'),
    ('wi', 'ti'),
    ('wi', 'wo'),
    ('pe', 'ca'),
    ('pe', 'do'),
]


def make_combos():
    combos = defaultdict(set)
    for (e1, e2) in tuples:
        combos[e1].add(e2)
        combos[e2].add(e1)
    return combos


def test(entries, combos):
    intersect = set(combos[entries[0]])
    for entry in entries[1:]:
        #print(combos[entry])
        intersect &= combos[entry]
    result = intersect if intersect else 'N/A'
    out = str(entries) + '=>' + str(result)
    print(out)
    return out

combos = make_combos()

assert test(['fm','sm'], combos) == "['fm', 'sm']=>{'pe', 'ca'}"
assert test(['sm','fm','pe'], combos) == "['sm', 'fm', 'pe']=>{'ca'}"
assert test(['sm','fm','wi'], combos) == "['sm', 'fm', 'wi']=>N/A"
