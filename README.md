# cbuveri
# Earthquake Data Visualization Demo

This is a simple demo application to visualize earthquake data in real-time.
- earthquake.py: This script scrapes earthquake data from the AFAD website, stores it in a CSV file, and runs in an infinite loop, continuously checking for new data every 5 minutes.
- earthquakevis.py: This script reads the CSV file created by earthquake.py, extracts the location data and displays a heatmap on a Flask web app using the Folium library.
- If you want to capture live data and view it at the same time, run it at the same time.
## Requirements

- Python 3.7 or higher
- Pandas
- Requests
- BeautifulSoup4
- Folium
- Flask
- Flask-DT

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries by running the command `pip install -r requirements.txt` in your terminal or command prompt.
3. Run the command `python earthquake.py` to start scraping data and storing it in a CSV file.
4. Open a new terminal or command prompt window and run the command `python earthquakevis.py` to start the Flask web app.
5. Navigate to `http://127.0.0.1:5000/iframe` in your web browser to view the earthquake heatmap.

## File Structure

- earthquake.py: The Python script that scrapes earthquake data and stores it in a CSV file.
- earthquakevis.py: The Python script that reads the CSV file and displays a heatmap on a Flask web app.
- templates/: This directory contains the HTML templates used by the Flask web app.
- static/: This directory contains the CSS and JavaScript files used by the HTML templates.

![Image](https://drive.google.com/uc?id=158LT4_fYjoA2ML0aBHQA6aAl72onMtjz)


## License

This project is licensed under the terms of the MIT license.

![Image](veri.jpg)
