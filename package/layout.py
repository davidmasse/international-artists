from package.traces import *
from package import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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
    )
])
