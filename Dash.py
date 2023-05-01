import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


import Balkendiagramm




app = dash.Dash()








app.layout = html.Div([
    dcc.Graph(
        id="Barchart",  
        figure= {
            "data": [Balkendiagramm.trace1, Balkendiagramm.trace2,Balkendiagramm.trace3],
            "layout": go.Layout(
                            title = "Average Delay per flight",
                            xaxis_tickfont_size=14,
                            yaxis=dict(
                                title='Delay in minutes',
                                titlefont_size=16,
                                tickfont_size=14),
                            legend=dict(
                                x=0,
                                y=1.0,
                                bgcolor='rgba(255, 255, 255, 0)',
                                bordercolor='rgba(255, 255, 255, 0)'),
                                barmode='group', 
                                bargap = 0.15, # Lücke zwischen den Balken der benachbarten Standortkoordinaten.
                                bargroupgap=0.05 # Lücke zwischen Balken derselben Standortkoordinate.

)
        
        
    }
    )
])

if __name__ == "__main__":
    app.run_server()