from package import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    songs = db.relationship('Song', back_populates='artist')

    def does_artist_have_show_in_country(self, countryname):
        country = Country.query.filter(Country.name == countryname).first()
        for show in country.shows:
            if show.songs[0].artist.name == self.name:
                return True
        return False

    def an_artists_number_of_countries(self):
        count = 0
        for c in Country.query.all():
            if self.does_artist_have_show_in_country(c.name):
                count += 1
        return count

    @classmethod
    def make_dict(cls):
        dict = {}
        for a in cls.query.all():
            dict.update({a.name: a.an_artists_number_of_countries()})
        return dict

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shows = db.relationship('Show', back_populates='country')

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    fmid = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    venue = db.Column(db.Text)
    city = db.Column(db.Text)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    songs = db.relationship('Song', secondary = 'show_song', back_populates = 'shows')
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country', back_populates='shows')

    @classmethod
    def venue_locations(cls):
       return {show.venue:[show.lat, show.lng] for show in Show.query.all()}

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    shows = db.relationship('Show', secondary='show_song', back_populates='songs')
    artist = db.relationship('Artist', back_populates='songs')
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

class ShowSong(db.Model):
    __tablename__ = 'show_song'
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), primary_key=True)

# db.create_all()
