import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


import Balkendiagramm
import Liniendiagramm
import Scatter
import Mapbox


app = dash.Dash()








app.layout = html.Div([
    dcc.Graph(
        id= "Liniendiagramm",
        figure= Liniendiagramm.fig
            ),
    dcc.Graph(
        id= "Scatterplot",
        figure= Scatter.fig
            ),
    dcc.Graph(
        id= "Balkendiagramm",
        figure= Balkendiagramm.fig1
            ),
    dcc.Graph(
        id= "Mapbox",
        figure= Mapbox.fig
            )
])
       


if __name__ == "__main__":
    app.run_server()