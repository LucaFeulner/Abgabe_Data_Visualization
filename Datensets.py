import pandas as pd

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Datenasätze____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


#df1 = pd.read_csv("Abgabe/res/all_flights_with_lon_and_lat.csv")

#df1 = df1[df1["MONTH"] == 1]
#-------------------------Datensets einlesen-------------------------
#df1 = pd.read_csv("https://gist.githubusercontent.com/florianeichin/cfa1705e12ebd75ff4c321427126ccee/raw/c86301a0e5d0c1757d325424b8deec04cc5c5ca9/flights_all_cleaned.csv", sep= ",")
#df2 = pd.read_csv("Abgabe/res/airports.csv", sep=";")
#df4 = pd.read_csv("Abgabe/res/airlines.csv")


#df4.rename(columns={"AIRLINE":"AIRLINE_NAME"}, inplace=True)


# Die drei Datensets  zun einem zusammenfügen
#df3 = pd.merge(df1, df2[['IATA_CODE', 'STATE']], left_on='ORIGIN_AIRPORT', right_on='IATA_CODE', how='left')
#df5 = pd.merge(df3, df4[["IATA_CODE", "AIRLINE_NAME"]], left_on="AIRLINE", right_on="IATA_CODE", how="left")

# Entferne die Spalte "IATA_CODE"
##df5.drop('IATA_CODE_x', axis=1, inplace=True)
#df5.drop('IATA_CODE_y', axis=1, inplace=True)

# Speichere das Ergebnis als CSV-Datei
#df5.to_csv("Abgabe/res/FertigesDatenset.csv", index=False)


