import plotly.graph_objects as go

layout_Barchart = go.Layout(
                            title = "Average Delay per flight",
                            xaxis_tickfont_size=14,
                            yaxis=dict(
                                title='Delay in minutes',
                                titlefont_size=16,
                                tickfont_size=14),
                            legend=dict(
                                x=0,
                                y=1.0,
                                bgcolor='rgba(255, 255, 255, 0)',
                                bordercolor='rgba(255, 255, 255, 0)'),
                                barmode='group', 
                                bargap = 0.15, # Lücke zwischen den Balken der benachbarten Standortkoordinaten.
                                bargroupgap=0.05 # Lücke zwischen Balken derselben Standortkoordinate.

                                )
