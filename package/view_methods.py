from package.models import *


from sqlalchemy import func, desc
import dash_core_components as dcc
import dash_html_components as html

from package.config import *
import plotly.graph_objs as go

def number_of_countries_visited():
    d = Artist.make_dict()
    ordered_tuples = list(sorted(d.items(), key = lambda pair: pair[1], reverse = True))[0:19]
    x = [o[0] for o in ordered_tuples]
    y = [o[1] for o in ordered_tuples]
    # artist = Artist.get(artist_id)
    # artist.does_artist_have_show_in_country()
    graphdata = [
        {'name': "Number of Countries Visited",
        'x': x,
        'y': y,
        'type': "bar"},
    ]
    return graphdata

def top10_venues_for_country(chosen_country):
    countryid = Country.query.filter(Country.name == chosen_country).first().id
    table_data = db.session.query(Show.venue, func.count(Show.venue), Show.city).group_by(Show.venue).order_by(desc(func.count(Show.venue))).filter(Show.country_id == countryid).all()[0:10]
    return html.Table(id='venue-table', children=
        [html.Tr(id='headers', children=[html.Th('Venue'), html.Th('Count'), html.Th('City')])] +
        [html.Tr(id='row-data', children=[html.Td(row[0]), html.Td(row[1]), html.Td(row[2])]) for row in table_data])

def venue_locations_for_artist(art):
    lat_lng_lists =[]
    for show in Show.query.all():
        if art == show.songs[0].artist.name:
            lat_lng_lists.append(Show.venue_locations()[show.venue])
    return lat_lng_lists

def lat_lng(art):
    lat = []
    lng = []
    for item in venue_locations_for_artist(art):
        lat.append(item[0])
        lng.append(item[1])
    return lat, lng

def list_of_venues(art):
   venue_list = []
   for show in Show.query.all():
       if art == show.songs[0].artist.name:
           venue_list.append(show.date + ', ' + show.venue + ', ' + show.city)
   return venue_list

def make_map(art):
    data = [
    go.Scattermapbox(
        lat=lat_lng(art)[0],
        lon=lat_lng(art)[1],
        mode='markers',
        marker=dict(
            size=8
        ),
        text = list_of_venues(art),
    )
    ]
    layout = go.Layout(
        autosize = False,
        hovermode = 'closest',
        width = 800,
        height = 500,
        mapbox = dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=30,
                lon=-210
            ),
            pitch=0,
            zoom=0.2
    ),
    )
    return [dcc.Graph(id = 'map', figure = dict(data=data, layout=layout))]
