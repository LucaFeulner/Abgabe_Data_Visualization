import plotly.graph_objects as go

import Layout
import pandas as pd
#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Mapbox____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________




# Abflughäfen auf einer Map anzeigen
# Größe der Punkte ist die Anzahl wie oft dort der Starts (pro Tag)
# Für eine bessere übersicht nur die größten 20 Flughafen

df = pd.read_csv("Abgabe/res/FertigesDatenset.csv")

# Datensatznach Abflughafren gruppiert und die Flugnummern gezählt
fluege_pro_flughafen = df.groupby("ORIGIN_AIRPORT")["FLIGHT_NUMBER"].count()

# Die 20 größten Flughafenkürzel in der variablen speichern
zwanzig_groeßten_Flughafen= fluege_pro_flughafen.nlargest(20).index



# neues kleines Datenset anlegen --> es werden nur die Zeilen aus dem großen Datenset genommen, wo  die kürzel mit der oben erstellten variable übereinstimmen
datenset_zwanzig = df[df["ORIGIN_AIRPORT"].isin(zwanzig_groeßten_Flughafen)]

