from package.setlist_data import data
from package.models import *
from package import db

for item in data:
    if item['artist']['name'] not in set([art.name for art in Artist.query.all()]):
        db.session.add(Artist(name = item['artist']['name']))
    artist = Artist.query.filter(Artist.name == item['artist']['name']).first()
    artistid = artist.id
    if item['id'] not in set([sh.fmid for sh in Show.query.all()]):
        db.session.add(Show(fmid = item['id'], date = item['eventDate'], venue = item['venue']['name'], city = item['venue']['city']['name'], lat = item['venue']['city']['coords']['lat'], lng = item['venue']['city']['coords']['long']))
    show = Show.query.filter(Show.fmid == item['id']).first()
    if item['venue']['city']['country']['name'] not in set([c.name for c in Country.query.all()]):
        db.session.add(Country(name = item['venue']['city']['country']['name']))
    country = Country.query.filter(Country.name == item['venue']['city']['country']['name']).first()
    country.shows.append(show)
    setlist = list(set([s['name'] for s in item['sets']['set'][0]['song']]))
    print(setlist)
#    db.session.commit()
    for songname in setlist:
        if songname not in set([so.name for so in artist.songs]):
            songtoadd = Song(name = songname)
            db.session.add(songtoadd)
            artist.songs.append(songtoadd)
        song = db.session.query(Song).filter_by(name = songname, artist_id = artistid).first()
        show.songs.append(song)
db.session.commit()



# for item in data:
#     if item['artist']['name'] not in set([art.name for art in Artist.query.all()]):
#         artist = Artist(name = item['artist']['name'])
#         db.session.add(artist)
#         db.session.commit()
#     if item['id'] not in set([sh.fmid for sh in Show.query.all()]):
#         show = Show(fmid = item['id'], date = item['eventDate'], venue = item['venue']['name'], city = item['venue']['city']['name'])
#         db.session.add(show)
#         db.session.commit()
#     if item['venue']['city']['country']['name'] not in set([c.name for c in Country.query.all()]):
#         country = Country(name = item['venue']['city']['country']['name'])
#         country.shows.append(show)
#         db.session.add(country)
#         db.session.commit()
#     setlist = list(set([s['name'] for s in item['sets']['set'][0]['song']]))
#     for songname in setlist:
#         import pdb; pdb.set_trace()
#         if songname not in set(artist.songs):
#             song = Song(name = songname)
#             artist.songs.append(song)
#             show.songs.append(song)
#             db.session.add(song)
#             db.session.commit()
