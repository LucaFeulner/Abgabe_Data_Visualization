import plotly.graph_objects as go

import Layout
import pandas as pd
#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Liniendiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

# Wie viele Flüge gab es im Januar in den 10 größten Flughäfen
# X-Achse 01.01.2015-31.01.15
# Y-Achse zusammengezählter Wert


# Fertiges Datenset was in Datensets.py bearbeitet wurde einlesen
df = pd.read_csv("Abgabe/res/FertigesDatenset.csv")

fluege_pro_airline = df.groupby("AIRLINE")["FLIGHT_NUMBER"].count()
zehn_groeßten_airlines = fluege_pro_airline.nlargest(10).index

datenset_zehn = df[df["AIRLINE"].isin(zehn_groeßten_airlines)]

farben = ["#143d59", "#e71989", "#b8df10", "#f6b60d", "#5e057e", "#a2eacb", "#761137", "#514644", "#0f4d19", "#104c91"]
farben_zaehler = 0
fig = go.Figure()

# Datenset das nach Airline und dann nach Tagen gruppiert wurde, und die Anzahl der Flugnummer zählt, da Flugnummern einmalig sind
fluege_anzahl = datenset_zehn.groupby(["AIRLINE", "DAY"])["FLIGHT_NUMBER"].count().reset_index()

for airline in fluege_anzahl["AIRLINE"].unique():
    fig.add_trace(go.Scatter(
                            x = fluege_anzahl[fluege_anzahl["AIRLINE"] == airline ]["DAY"],
                            y =fluege_anzahl[fluege_anzahl["AIRLINE"] == airline]["FLIGHT_NUMBER"],
                            name = airline,
                            line_color = farben[farben_zaehler]

                            
                            )
                )
    farben_zaehler = farben_zaehler +  1

fig.update_layout(  title="Anzahl der Flüge pro Tag und Fluggesellschaft im Januar 2015",
                    xaxis = dict(
                                tickvals = fluege_anzahl['DAY'].unique(),
                                gridcolor = "lightgray",
                                title = "Tag",
                                ),
                    yaxis = dict( 
                                title = "Anzahl der Flüge",
                                gridcolor = "lightgray"
                                ),
                    plot_bgcolor = "white"
                    )

fig.show()