from package import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from package.view_methods import *

from package.config import *
import plotly.graph_objs as go

graphdata = number_of_countries_visited()
map_dropdown = graphdata[0]['x'][0:5]

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
        id='map-selector',
        options=[
            {'label': map_dropdown[0], 'value': map_dropdown[0]},
            {'label': map_dropdown[1], 'value': map_dropdown[1]},
            {'label': map_dropdown[2], 'value': map_dropdown[2]},
            {'label': map_dropdown[3], 'value': map_dropdown[3]},
            {'label': map_dropdown[4], 'value': map_dropdown[4]}
        ],
        value = map_dropdown[0]
    ),
    html.H3("Tour Info"),
    html.Div(id='map-container'),
    dcc.Dropdown(
        id='selector',
        options=[
            {'label': 'United States', 'value': 'United States'},
            {'label': 'United Kingdom', 'value': 'United Kingdom'},
            {'label': 'Japan', 'value': 'Japan'},
            {'label': 'France', 'value': 'France'}
        ],
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
