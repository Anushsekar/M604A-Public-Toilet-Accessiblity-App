import plotly.express as px
import pandas as pd

df = pd.read_csv("Cordinates.csv")

# Drop any rows with missing values
df.dropna(axis=0, how='any', inplace=True)

# Define color scale for the Listed column
color_scale = [(0, 'orange'), (1, 'red')]

# Create scatter mapbox plot
fig = px.scatter_mapbox(df,
                        lat="Lat",
                        lon="Long",
                        hover_name="Address",
                        hover_data=["Address", "Listed"],
                        color="Listed",
                        color_continuous_scale=color_scale,
                        size="Listed",
                        zoom=8,
                        height=800,
                        width=800)

# Update layout to use open-street-map style
fig.update_layout(mapbox_style="open-street-map")

# Update layout to remove margins
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the plot
fig.show()