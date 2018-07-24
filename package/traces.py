from package.queries import *

def number_of_countries_visited():
    d = make_dict()
    ordered_tuples = list(sorted(d.items(), key = lambda pair: pair[1], reverse = True))
    x = [o[0] for o in ordered_tuples]
    y = [o[1] for o in ordered_tuples]
    artist = Artist.get(artist_id)
    artist.does_artist_have_show_in_country()
    graphdata = [
        {'name': "Number of Countries Visited",
        'x': x,
        'y': y,
        'type': "bar"},
    ]
    return graphdata
