from flask import Flask, render_template,render_template_string
import folium
import pandas as pd
from folium import plugins
from itables import init_notebook_mode
from itables import show
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
    data_coordinate = pd.read_csv("earthquakes.csv",usecols= ['Location','Latitude','Longitude'])
    locations = [(row['Latitude'], row['Longitude']) for index, row in data_coordinate.iterrows()]
    return locations

def get_heatmap():
    data_coordinate = pd.read_csv("earthquakes.csv",usecols= ['Location','Latitude','Longitude'])
    df=data_coordinate.copy()
    df["Latitude"]=df["Latitude"].astype(float)
    df["Longitude"]=df["Longitude"].astype(float)  # add a closing parenthesis here
    heat_df=df[["Latitude","Longitude"]]
    heat_data=list(zip(df["Latitude"], df["Longitude"]))
    return heat_data    
    


@app.route("/")
def base():
    map = folium.Map(
        location = getdata()[0]
    )
    plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)

  #  plugins.MarkerCluster(getdata()).add_to(map)
    return map.get_root().render()


@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    map = folium.Map(
        location = getdata()[0]
    )
    plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)
    
    data_coordinate = pd.read_csv("earthquakes.csv")
    df=data_coordinate.copy()
    
    # set the iframe width and height
    map.get_root().width = "100%"
    map.get_root().height = "100%"
    iframe = map.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                
               <style>
 /* Apply a general reset to the page */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Define the styles for the header */
header {
  background-color: #333;
  color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 10px; /* reduced padding */
}


/* Define the styles for the site logo */
.site-logo {
  flex: 1 0 auto;
  margin-right: 20px;
}

.site-logo img {
  height: 80px; /* keep image height */
}

/* Define the styles for the navigation */
nav {
  flex: 1 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-items: center;
}

nav ul {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  font-size: 16px;
}

.header-cases {
  background-color: #fff;
  color: #333;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  font-size: 16px;
  margin-left: 20px;
}

/* Define the styles for the boxes containing the iframes */
.box {
  width: 100%;
  max-width: 1024px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
}

/* Define the styles for the iframes */
.box iframe {
  width: 100%;
  height: 512px;
}

/* Define the styles for the footer */
footer {
  background-color: #ccc;
  color: #333;
  padding: 20px;
  text-align: center;
}

/* Define the media queries for smaller screens */
@media (max-width: 768px) {
  header {
    flex-direction: column;
    text-align: center;
    padding: 20px 10px; /* increase padding for balance */
  }

  .site-logo {
    margin-bottom: 20px;
  }

  nav {
    margin-top: 20px;
    justify-content: center;
  }

  .header-cases {
    margin-left: 0;
    margin-top: 20px;
  }

  .box {
    flex-direction: column;
    align-items: center;
  }

  img {
    height: 80px; /* keep image height */
    max-width: 100%;
    width: 200px;
  }
}
</style>
                </head>
                <body>
                  <header>
      <div class="site-logo">
     <img src="https://drive.google.com/uc?export=view&id=1oMB0oUadS7eK-4pWk1_4OQiuZnYZTViM" alt="your image description">

      </div>
    
              <h2>Deprem Veri Görselleştirme DEMO</h2>
              
               <nav>

    <ul>
      <li><a href="#">Depremler</a></li>
      <li><a href="#">Hakkımızda</a></li>
      <li><a href="#">İletişim</a></li>
    </ul>
  </nav>
                       </header>
                    
                    
             
                
<div class="box">
  <iframe src="{{ url_for('map_content') }}" frameborder="0" scrolling="no" height="512" align="left"> </iframe>
</div>

<div class="box">
  <iframe src="{{ url_for('components') }}" frameborder="0" scrolling="no" height="512" align="right"></iframe>
</div>
                
                    
                </body>
                 <footer>
                      <p>@cbüVERİ 2023</p>
                     </footer>
            </html>
           
        """
    )
@app.route("/components")
def components():
    data = pd.read_csv("earthquakes.csv")
    #init_notebook_mode(all_interactive=True)
    table_html = DT(data, css_class='display')

    return render_template('table.html', table_html=table_html)

        
@app.route("/map")
def map_content():
    map = folium.Map(
        location=getdata()[0]
    )
    plugins.HeatMap(get_heatmap(), overlay_name='').add_to(map)

    # set the iframe width and height
    map.get_root().width = "100%"
    map.get_root().height = "100%"
    iframe = map.get_root()._repr_html_()

    return iframe



if __name__ == 'main':
    
    app.run(debug=True)
    