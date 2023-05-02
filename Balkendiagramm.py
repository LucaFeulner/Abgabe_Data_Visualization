import plotly.graph_objects as go

import Layout
import pandas as pd
#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Balkendiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

# Balkendiagramm durchschnittliche aufgeholte Zeit pro Flug
#X-Achse Kurzstrec kenflüge bis <= 1.000, Mittelstrecke >1000 und <= 3000, Langstrecke > 3000.
#Y-Achse durchschnittliche verspätung pro flug in Minuten
#Beim Drüber hovern soll die Airline angezeigt werden und an der Seite gibt es eine legende mit den Farben für kurz und langstrecke


# Filter durchschnitt, ankunft , verspätung

# Datenset aus Datensets.py importieren 
df = pd.read_csv("Abgabe/res/AbgabeDatenset.csv")




short_haul_flight = go.Bar(name = "Kurzstreckenflug", x = df["AIRLINE"])
df["DELAY"] = df["SCHEDULED_TIME"]-df["ELAPSED_TIME"]
avg_delay = df.groupby("AIRLINE")["DELAY"].mean()
airline_group = df["AIRLINE"].unique()

# Festlegen, ab welcher Distanz welche Art von Flug ist
short_haul = df[df["DISTANCE"] <= 1000]
medium_haul = df[(df["DISTANCE"] <= 3000) & (df["DISTANCE"] > 1000)]
long_haul = df[df["DISTANCE"] >3000]

# Berechnen der durchschnittlichen Verspätung pro Flug
short_haul_avg_delay = short_haul.groupby("AIRLINE")["DELAY"].mean()
medium_haul_avg_delay = medium_haul.groupby("AIRLINE")["DELAY"].mean()
long_haul_avg_delay = long_haul.groupby("AIRLINE")["DELAY"].mean()

fig1 = go.Figure()

# Balken für die Kurzstrecke
trace1 = go.Bar(
    x = airline_group,
    y = short_haul_avg_delay,
    name = "short_haul",
    marker_color='rgb(118, 204, 122)'
)

# Balken für die Mittelstrecke
trace2 = go.Bar(
    x = airline_group,
    y = medium_haul_avg_delay,
    name = "medium_haul",
    marker_color= 'rgb(26, 118, 255)'

)

# Balken für die Langstrecke
trace3 = go.Bar(
    x = airline_group,
    y = long_haul_avg_delay,
    name = "long_haul",
    marker_color='rgb(55, 83, 109)',
    
)


# Style für das Balkendiagramm
layout = go.Layout(
    title = "Average airtime difference",
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Delay in minutes',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group', 
    bargap = 0.15, # Lücke zwischen den Balken der benachbarten Standortkoordinaten.
    bargroupgap=0.05 # Lücke zwischen Balken derselben Standortkoordinate.

)

fig1.add_trace(trace1)
fig1.add_trace(trace2)
fig1.add_trace(trace3)

fig1 = go.Figure(data=[trace1,trace2, trace3], layout= Layout.layout_Barchart)


fig1.update_layout(
    updatemenus = [
        dict(
            active = 0, 
            buttons = list([
                dict(label = "None",
                     method = "update",
                     args = [{"visible": [True, True, True]},
                             {"title": "Average Delay per Flight"}]),

                dict(label = "Short_haul",
                     method = "update",
                     args = [{"visible": [True, False, False]},
                             {"title": "Average Delay per short Flight"}],
                       ),
                dict(label = "Mid_haul",
                     method = "update",
                     args = [{"visible": [False, True, False]},
                             {"title": "Average Delay per short Flight"}],
                       ),
                dict(label = "Long_haul",
                     method = "update",
                     args = [{"visible": [False, False, True]},
                             {"title": "Average Delay per short Flight"}],
                       )
        ])
             )
    ]
)

