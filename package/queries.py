from package.models import *

def does_artist_have_show_in_country(artistname, countryname):
    country = Country.query.filter(Country.name == countryname).first()
    for show in country.shows:
        if show.songs[0].artist.name == artistname:
            return True
    return False

def make_dict():
    dict = {}
    for a in Artist.query.all():
        dict.update({a.name: 0})
        for c in Country.query.all():
            if does_artist_have_show_in_country(a.name, c.name):
                dict[a.name] += 1
    return dict
