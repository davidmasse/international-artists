from package import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from package.view_methods import *

from package.config import *
import plotly.graph_objs as go

graphdata = number_of_countries_visited()
map_dropdown = graphdata[0]['x'][0:5]
cs = [country.name for country in Country.query.all()]

app.layout = html.Div(children=[
    html.H3("Setlist Stats"),
    dcc.Graph(
        id = "most intl",
        figure = {
            'data': graphdata,
            'layout': {
                'title': "Most International Musicians"
            }
        }
    ),
    dcc.Dropdown(
        id = 'map-selector',
        options = [{'label':mapdrop, 'value':mapdrop} for mapdrop in map_dropdown],
        value = 'Please select an artist.'
    ),
    html.H3("Tour Info"),
    html.Div(id='map-container'),
    dcc.Dropdown(
        id='selector',
        options=[{'label': c, 'value': c} for c in cs],
        value="United States"
    ),
    html.H3("Top Concert Venues for Chosen Country"),
    html.Div(id='table-container')
])

@app.callback(
    Output(component_id='table-container', component_property='children'),
    [Input(component_id='selector', component_property='value')]
)

def choose_country(input_value):
    return top10_venues_for_country(input_value)

@app.callback(
    Output(component_id='map-container', component_property='children'),
    [Input(component_id='map-selector', component_property='value')]
)

def choose_map(input_value):
    return make_map(input_value)
