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



url_staaten = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
token = 'pk.eyJ1IjoibHVjYWYyMDAyIiwiYSI6ImNsZm1sdmg2bTBkMG8zeG5wbmNkMmRmeXcifQ.6tnXcyV6b870rKIE023_pw'


#----------Jasondaten in die Variable geo_data laden
with urlopen(url_staaten) as response:
    geo_data = json.load(response)

#----------Namen der einzelen Staaten raussuchen um diese dann mit dem Datenset zu verbinden
for feature in geo_data['features']:
    feature['id'] = feature['properties']['name']




fig = go.Figure()

df_staaten_mean  = df.groupby("State").mean()


#----------Jasondatei auf die Map bringen
a = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_mean.index,
                    z =  df_staaten_mean.FLIGHT_NUMBER,
                    marker_opacity=0.7,
                    marker_line_width=1,
                    colorscale='GnBu'
                    
    )


fig.add_trace(a)



fig.update_layout(
                    mapbox_accesstoken = token,
                    mapbox_style = "light",
                    mapbox_zoom = 2.8,
                    mapbox_center={"lat": 37.090240, "lon": -95.712891}
    )
















fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


fig.show()
