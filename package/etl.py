from package.setlist_data import data
from package.models import *

def make_artists(data):
    list_of_artists = []
    for item in data:
        if item['artist']['name'] not in set([art.name for art in list_of_artists]):
            list_of_artists.append(Artist(name = item['artist']['name']))
    return list_of_artists

def assign_an_artists_songs(anartist, data):
    list_of_songs = []
    list_of_song_names = []
    for item in data:
        if item['artist']['name'] == anartist.name:
            list_of_song_names = list_of_song_names + [s['name'] for s in item['sets']['set'][0]['song']]
            list_of_song_names = list(set(list_of_song_names))
    for song_name in list_of_song_names:
        temp_song = Song(name = song_name)
        list_of_songs.append(temp_song)
    return list_of_songs

def finished_artists():
    list_of_artists_with_songs = []
    artists = make_artists(data)
    for a in artists:
        a.songs = assign_an_artists_songs(a, data)
        list_of_artists_with_songs.append(a)
    return list_of_artists_with_songs

def make_countries(data):
    list_of_countries = []
    for item in data:
        if item['venue']['city']['country']['name'] not in set([c.name for c in list_of_countries]):
            list_of_countries.append(Country(name = item['venue']['city']['country']['name']))
    return list_of_countries

def make_shows(data):
    list_of_shows = []
    for item in data:
        if item['id'] not in set([sh.fmid for sh in list_of_shows]):
            list_of_shows.append(Show(fmid = item['id'], date = item['eventDate'], venue = item['venue']['name'], city = item['venue']['city']['name']))
    return list_of_shows

def assign_a_countrys_shows(acountry, data):
    list_of_shows = []
    for item in data:
        if item['venue']['city']['country']['name'] == acountry.name:
            for show in shows:
                if show.fmid == item['id']:
                    list_of_shows.append(show)
    return list_of_shows

def finished_countries():
    list_of_countries_with_shows = []
    for c in countries:
        c.shows = assign_a_countrys_shows(c, data)
        list_of_countries_with_shows.append(c)
    return list_of_countries_with_shows

def assign_a_songs_shows(asong, data):
    list_of_shows = []
    for item in data:
        songnames = [s['name'] for s in item['sets']['set'][0]['song']]
        songnames = set(songnames)
        for show in shows:
            if item['id'] == show.fmid and asong.name in songnames and asong.artist.name == item['artist']['name']:
                list_of_shows.append(show)
    return list_of_shows

def finished_songs(artists):
    list_of_songs_with_shows = []
    for art in artists:
        for s in art.songs:
            s.shows = assign_a_songs_shows(s, data)
            list_of_songs_with_shows.append(s)
    return list_of_songs_with_shows


artists = finished_artists()
shows = make_shows(data)
countries = make_countries(data)

db.session.add_all(artists)

db.session.add_all(finished_countries())
db.session.add_all(finished_songs(artists))
db.session.commit()
    # make all artist objets
    # make all song objects, and assign to artist
    # make all shows, make show song relationship
    # all_countries = make countries
    # relates countries and shows (country and all shows)
    # add
    # commit
