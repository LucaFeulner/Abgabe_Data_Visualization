import pandas as pd
import numpy as np
import plotly.graph_objects as go
import Datensets

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Scatterplot____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


#besteht ein zusammenhang zwischen der länge des fluges und der verspätung




#besteht ein zusammenhang zwischen der länge des fluges und der verspätung

df_short = Datensets.df5.query("DISTANCE < 1000")
df_mid = Datensets.df5.query("1000 < DISTANCE <= 3000")

fig = go.Figure()



trace1 = go.Scatter(
    x = df_short["DISTANCE"],
    y = df_short["DESTINATION_DELAY"],
    mode = "markers",
    marker_color = "rgb(51,204,153)"
)

trace2 = go.Scatter(
    x = df_mid["DISTANCE"],
    y = df_mid["DESTINATION_DELAY"],
    mode = "markers"
    

)


fig.add_trace(trace1)
fig.add_trace(trace2)

# xaxis = go.layout.XAxis(type="log")
#yaxis = go.layout.YAxis(type="log")
#fig.update_layout (yaxis=yaxis)

fig.show()