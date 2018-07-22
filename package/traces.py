from package.queries import *

d = make_dict()
ordered_tuples = list(sorted(d.items(), key = lambda pair: pair[1]))
x = [o[0] for o in ordered_tuples]
y = [o[1] for o in ordered_tuples]

graphdata = [
    {'name': "Number of Countries Visited",
    'x': x,
    'y': y,
    'type': "bar"},
]
