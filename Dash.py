import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


import Balkendiagramm



app = dash.Dash()








app.layout = html.Div([
    dcc.Graph(
        id= "Verspätung-pro-Flug",
        figure= Balkendiagramm.fig1
            ),
        dcc.Graph(
            id="Scatterplot",
            figure= {
            "data": [],
            "layout": go.Layout()
            }
        )
])


if __name__ == "__main__":
    app.run_server()