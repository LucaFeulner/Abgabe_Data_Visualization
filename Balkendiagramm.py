import plotly.graph_objects as go
import Datensets


df = Datensets.df5

#Geschschteltes Balkendiagramm durchschnittliche verspätete Zeit pro Flug
#X-Achse Kurzstrec kenflüge bis <= 1.500Km, Rest ist Langstrecke
#Y-Achse durchschnittliche verspätung pro flug
#Beim Drüber hovern soll die Airline angezeigt werden und an der Seite gibt es eine legende mit den Farben für kurz und langstrecke



short_haul_flight = go.Bar(name = "Kurzstreckenflug", x = df["AIRLINE"])
df["DELAY"] = df["DEPARTURE_DELAY"]-df["DESTINATION_DELAY"]
avg_delay = df.groupby("AIRLINE")["DELAY"].mean()
airline_group = df["AIRLINE"].unique()

short_haul = df[df["DISTANCE"] <= 1000]
medium_haul = df[(df["DISTANCE"] <= 3000) & (df["DISTANCE"] > 1000)]
long_haul = df[df["DISTANCE"] >3000]

short_haul_avg_delay = short_haul.groupby("AIRLINE")["DELAY"].mean()
medium_haul_avg_delay = medium_haul.groupby("AIRLINE")["DELAY"].mean()
long_haul_avg_delay = long_haul.groupby("AIRLINE")["DELAY"].mean()




trace1 = go.Bar(
    x = airline_group,
    y = short_haul_avg_delay,
    name = "short_haul",
    marker_color='rgb(118, 204, 122)'
)

trace2 = go.Bar(
    x = airline_group,
    y = medium_haul_avg_delay,
    name = "medium_haul",
    marker_color= 'rgb(26, 118, 255)'

)

trace3 = go.Bar(
    x = airline_group,
    y = long_haul_avg_delay,
    name = "long_haul",
    marker_color='rgb(55, 83, 109)'
)



layout = go.Layout(
    title = "Average Delay per flight",
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



