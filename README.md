# cbuveri
Earthquake Data Scraper and Visualizer
This is a Python web application that scrapes earthquake data from the Turkish Disaster and Emergency Management Presidency website and visualizes it using the Folium library.

The code consists of two files:

earthquake.py: This script scrapes the earthquake data every 5 minutes and appends the new data to a CSV file.
earthquakevis.py: This script loads the CSV data, creates a heatmap using the Folium library, and displays it on a web page.
Requirements
Python 3.7 or later
Pandas library
Requests library
BeautifulSoup library
Folium library
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/example/earthquake-scraper.git
Install the required libraries:

Copy code
pip install pandas requests beautifulsoup4 folium
Start the application:

Copy code
python earthquakevis.py
Open your web browser and navigate to http://localhost:5000/ to view the earthquake heatmap.

Usage
The application will automatically scrape earthquake data every 5 minutes and append the new data to the earthquakes.csv file. To view the latest earthquake data, simply refresh the web page.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
