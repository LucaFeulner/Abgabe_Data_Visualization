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

zehn_groeßte_airline = df.groupby("AIRLINE")["FLIGHT_NUMBER"].count()
zehn_groeßte_airline = zehn_groeßte_airline.reset_index()
zehn_groeßte_airline = zehn_groeßte_airline.rename(columns={"FLIGHT_NUMBER" : "count"})
zehn_groeßte_airline = zehn_groeßte_airline.sort_values(by ="count", ascending= False)
zehn_groeßte_airline  = zehn_groeßte_airline.reset_index()
zehn_groeßte_airline = zehn_groeßte_airline.loc[zehn_groeßte_airline['count'] >= 13151]
zehn_groeßte_airline = zehn_groeßte_airline[["AIRLINE", "count"]]



fig = go.Figure()

# Datenset das nach Airline und dann nach Tagen gruppiert wurde, und die Anzahl der Flugnummer zählt, da Flugnummern einmalig sind
fluege_anzahl = df.groupby(["AIRLINE", "DAY"])["FLIGHT_NUMBER"].count().reset_index()

for airline in fluege_anzahl["AIRLINE"].unique():
    fig.add_trace(go.Scatter(
                            x = fluege_anzahl[fluege_anzahl["AIRLINE"] == airline ]["DAY"],
                            y =fluege_anzahl[fluege_anzahl["AIRLINE"] == airline]["FLIGHT_NUMBER"]
                            
    )




    )

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