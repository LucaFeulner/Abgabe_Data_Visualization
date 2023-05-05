import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import json

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Mapbox____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________



#----------Datensets einlesen----------
df = pd.read_csv("Abgabe/res/FertigesDatenset.csv")
df1 = pd.read_csv("Abgabe/res/staates.csv", sep=",")

#----------Da in der jason Datei die Bundesstaaten ausgeschrieben  sind  musste ich die Ausgeschriebenen Staatennamen noch in das Datenset einfügen
df = pd.merge(df, df1[['Postal', 'State']], left_on='STATE', right_on='Postal', how='left')

#----------Spalte mit den abkürzungen doppelt also raus
df.drop('Postal', axis=1, inplace=True)

fluege_pro_flughafen = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count()
zwanzig_groeßten_flughafen = fluege_pro_flughafen.nlargest(20).index
groeße = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index(name="fluege").sort_values("fluege")

df_20 = df[df["AIRPORT"].isin(zwanzig_groeßten_flughafen)]
anzahl_fluege_top20_flughafen = df_20.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index()






url_staaten = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
token = 'pk.eyJ1IjoibHVjYWYyMDAyIiwiYSI6ImNsZm1sdmg2bTBkMG8zeG5wbmNkMmRmeXcifQ.6tnXcyV6b870rKIE023_pw'


#----------Jasondaten in die Variable geo_data laden
with urlopen(url_staaten) as response:
    geo_data = json.load(response)

#----------Namen der einzelen Staaten raussuchen um diese dann mit dem Datenset zu verbinden
for feature in geo_data['features']:
    feature['id'] = feature['properties']['name']




fig = go.Figure()

df_staaten_count  = df.groupby("State").count()


#----------Jasondatei auf die Map bringen
a = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_count.index,
                    z =  df_staaten_count["FLIGHT_NUMBER"],
                    marker_opacity=0.6,
                    marker_line_width=1,
                    colorscale='GnBu',
                    colorbar= dict(
                                    title = "Anzahl Flüge",
                                    titleside ="top"
                    )

                    
    )

b = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_count.index,
                    z = df_staaten_count["FLIGHT_NUMBER"],
                    marker_opacity=0.2,
                    marker_line_width=1,
                    visible=False,
                    colorscale= [[0, '#ffffff'], [0.5, '#ffffff'], [1.0, 'rgb(255, 255, 255)']],
                    showscale = False
                    

                    
    )



flughafen = go.Scattermapbox(
    lat = df_20['ORIGIN_AIRPORT_LAT'],
    lon= df_20['ORIGIN_AIRPORT_LON'],
    mode= "markers" ,
    marker=go.scattermapbox.Marker(
        size=groeße["fluege"]/30,
        color="#000000",
        sizemode="area",
        showscale=False,
        ) ,
    text=df['AIRPORT']   
)



fig.add_trace(a)
fig.add_trace(b)
fig.add_trace(flughafen)

fig.update_layout(
                    title = "Anzahl der Flüge nach Staaten(farbig) und Flughäfen",
                    xaxis = dict(
                                title = "Tag"
                                ),
                    mapbox_accesstoken = token,
                    mapbox_style = "light",
                    mapbox_zoom = 2.8,
                    mapbox_center={"lat": 37.090240, "lon": -95.712891}
    )


fig.update_layout(
    updatemenus = [
        dict(
            active = 0, 
            buttons = list([
                dict(label = "Staaten farbig",
                     method = "update",
                     args = [{"visible": [True, False, True]},
                             {"title": "Anzahl der Flüge nach Staaten(farbig) und Flughäfen"}
                             ]
                    
                        ),
                        

                dict(label = "Staaten ohne Farbe",
                     method = "update",
                     args = [{"visible": [False, True, True]},
                             {"title": "Anzahl der Flüge nach Staaten(SW) und Flughäfen"}
                             ],
                       )
                    
                    ]),
                xanchor = "left",
                x = 0,
                y= 1.05,
                yanchor = "top",
                
             ),
        dict(
            active = 0, 
            buttons = list([
                dict(label = "Flughäfen farbig",
                     method = "update",
                     args = [{"visible": [True, False, True]},
                             {"title": "Anzahl der Flüge nach Staaten(farbig) und Flughäfen"}
                             ]
                    
                        ),
                        

                dict(label = "Flughäfen ohne Farbe",
                     method = "update",
                     args = [{"visible": [False, True, True]},
                             {"title": "Anzahl der Flüge nach Staaten(SW) und Flughäfen"}
                             ],
                       )
                    
                    ]),
                xanchor = "left",
                x = 0.1,
                y= 1.05,
                yanchor = "top",
                
             )
        
    ],

    title_x = 0.5
)













fig.update_layout(margin={"r": 70, "t": 70, "l": 70, "b": 70})


fig.show()


