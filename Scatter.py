import pandas as pd
import plotly.graph_objects as go

import versuch

df = versuch.df
#----------20 größten Flughafen filtern
counts = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index(name = "Anzahl Flüge")
counts = counts.sort_values("Anzahl Flüge", ascending=False)
top20 = counts.head(20)

df_top20 = df[df["AIRPORT"].isin(top20["AIRPORT"].tolist())]

anzahl_top20= df_top20.groupby(["AIRPORT", "DAY"])["FLIGHT_NUMBER"].count().reset_index(name="Anzahl Flüge")
print(df_top20)

data  = []
for i, flughafen in enumerate(anzahl_top20["AIRPORT"].unique()):
    anzahl = anzahl_top20[anzahl_top20["AIRPORT"] == flughafen]
    print(anzahl)
    trace = go.Scatter(
        x = anzahl["DAY"],
        y = anzahl["Anzahl Flüge"],
        name = flughafen,
        mode = "markers",
        marker = dict(
            size = anzahl["Anzahl Flüge"]/40*2,
            sizemin = 3,
            line = dict(
                    width= 1,
                    color =  "DarkSlateGrey"
            )
        )
    )
    data.append(trace)

layout = go.Layout(
    title = "Flugzahlen pro Flughafen und pro Tag",
    xaxis = dict(
            title =  "Tage im Januar"
                ),
    yaxis= dict(
            title = "Anzahl der Flüge"
                )
)

fig = go.Figure(data = data,layout=layout)

fig.show()