from flask import Flask, render_template, render_template_string, request
import folium
import pandas as pd
from folium import plugins
from itables import to_html_datatable as DT

__author__ = "Mehmet Batuhan Duman, Ali Osman Beker"

vericbu = '''

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@**.#......*&***#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@.#@@@@@%@*/**@@@(/@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@./@,@@@***.@@*@@.&*@@.@,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@/*.*@,@@*@@@@@@/@@@**@*@@,,.*@@@@@@@@@@@@@@@@@@@@@@@***&@@@
@@.@..@**@@/,&&**%@///@@*@@.,/@@@@@@@@@@@@@@@@@@@@@@@%*(@@@@
@@.#@@@/@@/.@@@@,@*****@.@****@********@@*********@@@****@@@
@@/@@**&@,...***@@@*****@****@@****@@@@@@****@#***/@@****@@@
@@@(.@(*@.**@@.@@@@@,*******@@@********@@********@@@@****@@@
@@@@@/*@,@@@.@@@@@@@@******%@@@****@@@@@@****@****@@@****@@@
@@@@@@@%@@,*@@@@@@@@@@*****@@@@********@@****@@*****@****@@@
@@@@@@@@@@@@************************************************
@@@@@@@@@@@@*******Manisa Celal Bayar Universitesi********
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2023
'''

print(vericbu)

app = Flask(__name__)


def getdata():
    data_coordinate = pd.read_csv("earthquakes.csv", usecols=['Location', 'Latitude', 'Longitude','Type','Magnitude'])
    locations = [(row['Latitude'], row['Longitude'], row['Location'],row['Type'],row['Magnitude']) for index, row in data_coordinate.iterrows()]
    return locations


def get_heatmap():
    data_coordinate = pd.read_csv("earthquakes.csv", usecols=['Location', 'Latitude', 'Longitude'])
    df = data_coordinate.copy()
    df["Latitude"] = df["Latitude"].astype(float)
    df["Longitude"] = df["Longitude"].astype(float)
    heat_data = list(zip(df["Latitude"], df["Longitude"]))
    return heat_data

@app.route("/change_style/<style>")
def change_style(style):
    """Change the map style based on the user selection."""
    map = folium.Map(location=getdata()[0][0:2], tiles=style)

    for location in getdata():
        folium.Circle(
            location=location[0:2],
            radius=300,
            fill=True,
            tooltip=(location[2],) + (' ',) + (location[3],)+(' ',) + (location[4],)
        ).add_to(map)

    # set the iframe width and height
    map.get_root().width = "100%"
    map.get_root().height = "100%"

    iframe = map.get_root()._repr_html_()
    return iframe


@app.route("/")
def base():
    map = folium.Map(
        location=getdata()[0][0:2]
    )
    #plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)

    plugins.MarkerCluster(getdata()[0:2]).add_to(map)

    for location in getdata():
        folium.Circle(location=location[0:2],
                      radius=300,  # in meters
                      fill=True,
                      tooltip=(location[2],) + (' ',) + (location[3],)+(' ',) + (location[4],)
                      ).add_to(map)

    return map.get_root().render()


@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    map = folium.Map(
        location=getdata()[0][0:2]
    )
    plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)

    data_coordinate = pd.read_csv("earthquakes.csv")
    df = data_coordinate.copy()

    # set the iframe width and height
    map.get_root().width = "100%"
    map.get_root().height = "100%"
    iframe = map.get_root()._repr_html_()

    return render_template("iframe.html", iframe=map._repr_html_())


@app.route("/components")
def components():
    data = pd.read_csv("earthquakes.csv")
    # init_notebook_mode(all_interactive=True)
    table_html = DT(data, css_class='display')

    return render_template('table.html', table_html=table_html)


@app.route("/map")
def map_content():
    map = folium.Map(
        location=getdata()[0][0:2]
    )
    plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)

    map.get_root().width = "100%"
    map.get_root().height = "100%"
    for location in getdata():
        folium.Circle(location=location[0:2],
                      radius=300,  # in meters
                      fill=True,
                      tooltip=(location[2],) + (' ',) + (location[3],)+(' ',) + (location[4],)
                      ).add_to(map)
    iframe = map.get_root()._repr_html_()

    return iframe


if __name__ == 'main':
    app.run(debug=True)
