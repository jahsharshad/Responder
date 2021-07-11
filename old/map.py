from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'ERS':'Emergency Response Times'},
                          )

fig.update_traces(marker_line_width=0, marker_opacity=0.8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(showsubunits=True, subunitcolor="black")

fig.add_scattermapbox(lat = [37.548], lon = [-121.988], name = '', mode='markers', text = 'You are here', marker_size = 10, marker_color = 'rgb(235,0,100)')

# import requests
# import csv
#
# def getCounties(code):
#     "Function to return a dict of FIPS codes (keys) of U.S. counties (values)"
#     d = {}
#     r = requests.get("http://www2.census.gov/geo/docs/reference/codes/files/national_county.txt")
#     reader = csv.reader(r.text.splitlines(), delimiter=',')
#     for line in reader:
#         d[line[1] + line[2]] = line[3].replace(" County","")
#     return d[code]
#
# fips = df['fips']
#
# for i in range(len(fips)):
#     fips[i] = getCounties(fips[i])

#
#
#


# fig.show()

# fig.write_html("C:/Users/jahsh/Documents/jahsh/Programming/ExamplePlotlyGraph/Templates/Chart1.html")
