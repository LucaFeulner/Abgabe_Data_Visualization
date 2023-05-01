import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.offline as pyo
from dash.dependencies import Input, Output



app = dash.Dash()

df1 = pd.read_csv("https://gist.githubusercontent.com/florianeichin/cfa1705e12ebd75ff4c321427126ccee/raw/c86301a0e5d0c1757d325424b8deec04cc5c5ca9/flights_all_cleaned.csv", sep= ",")
df2 = pd.read_csv("Abgabe/airports.csv", sep=";")


df3 = pd.merge(df1, df2[['IATA_CODE', 'STATE']], left_on='ORIGIN_AIRPORT', right_on='IATA_CODE', how='left')

# Entferne die Spalte "IATA_CODE"
df3.drop('IATA_CODE', axis=1, inplace=True)

# Speichere das Ergebnis als CSV-Datei
df3.to_csv("flights_with_states.csv", index=False)

short_haul_flight = go.Bar(name = "Kurzstreckenflug", x = df3["AIRLINE"])
df3["DELAY"] = df3["DEPARTURE_DELAY"]-df3["DESTINATION_DELAY"]
avg_delay = df3.groupby("AIRLINE")["DELAY"].mean()
airline_group = df3["AIRLINE"].unique()

short_haul = df3[df3["DISTANCE"] <= 1000]
medium_haul = df3[(df3["DISTANCE"] <= 3000) & (df3["DISTANCE"] > 1000)]
long_haul = df3[df3["DISTANCE"] >3000]

short_haul_avg_delay = short_haul.groupby("AIRLINE")["DELAY"].mean()
medium_haul_avg_delay = medium_haul.groupby("AIRLINE")["DELAY"].mean()
long_haul_avg_delay = long_haul.groupby("AIRLINE")["DELAY"].mean()




trace1 = go.Bar(
    x = airline_group,
    y = short_haul_avg_delay,
    name = "short_haul",
    marker_color='rgb(55, 83, 109)'
)

trace2 = go.Bar(
    x = airline_group,
    y = long_haul_avg_delay,
    name = "long_haul",
    marker_color='rgb(26, 118, 255)'
)

trace3 = go.Bar(
    x = airline_group,
    y = medium_haul_avg_delay,
    name = "medium_haul"
)

data = [trace1, trace3 ,trace2]




app.layout = html.Div([
    dcc.Dropdown(
        id='state-dropdown',
        options= df3["STATE"].unique(),
        value=[],
        multi=True
    ),
    dcc.Graph(
        id="Barchart",
        figure= {
            "data": [trace1, trace3,trace2],
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
@app.callback(
    Output("Barchart", "figure"),
    Input("state-dropdown", "value")
)
def update_barchart(states):
    print("hi")
    if not states:
        filtered_df = df3
    else:
        filtered_df = df3[df3["STATE"].isin(states)]
    
    # Fügen Sie hier den Rest des Codes zur Diagrammerstellung mit den gefilterten Daten ein
    

    return {"data": data, "layout": go.Layout}


if __name__ == "__main__":
    app.run_server()