import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
print(vericbu)
# Deprem verisini çeker
def scrape_earthquake_data():
    url = 'https://deprem.afad.gov.tr/last-earthquakes.html'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # table'ı bulur ve tüm satırları döngüye alır
    table = soup.find('table', {'class': 'content-table'})
    rows = table.find_all('tr')[1:]  # skip the header row

    #satır verilerini array'de tutmak için
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    # pandas'ı kullanarak bir adet dataframe oluşturma
    df = pd.DataFrame(data, columns=['Date/Time', 'Latitude', 'Longitude', 'Depth', 'Type', 'Magnitude', 'Location', 'ID'])

    return df

# # deprem verilerini dataframme'den alıp csv'ye yazma
# def write_to_csv(df):
#     # hali hazırda csv'deki verileri tekrar güncelleme sırasında okuma
#     try:
#         existing_data = pd.read_csv('earthquakes.csv')
#     except FileNotFoundError:
#         existing_data = pd.DataFrame(columns=df.columns)

#     # yeni veriyi eskisi ile karşılaştırma
#     diff_df = df[~df.isin(existing_data)].dropna()
#     if not diff_df.empty:
#         # yeni veri varsa csv'ye ekleme
#         updated_data = pd.concat([existing_data, diff_df])
#         updated_data.to_csv('earthquakes.csv', index=False)
#         print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} New data appended to the CSV file.')
#     else:
#         print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} No new data found.')

# # ana döngü'de her 5 dakikada bir çalıştırma
# while True:
#     df = scrape_earthquake_data()
#     write_to_csv(df)
#     time.sleep(300)  # 5 dakika bekleme
# deprem verilerini dataframme'den alıp csv'ye yazma
#-------------------------------------------------------
# def write_to_csv(df):
#     # hali hazırda csv'deki verileri tekrar güncelleme sırasında okuma
#     try:
#         existing_data = pd.read_csv('earthquakes.csv')
#     except FileNotFoundError:
#         existing_data = pd.DataFrame(columns=df.columns)

#     # yeni veriyi eskisi ile karşılaştırma
#     # diff_df = df[~df.isin(existing_data)].dropna()
#     # use a unique identifier for each earthquake instead of comparing all columns
#     diff_df = df[~df['Date/Time'].isin(existing_data['Date/Time'])] # use 'Date/Time' instead of 'date_time'
#     if not diff_df.empty:
#         # yeni veri varsa csv'ye ekleme
#         updated_data = pd.concat([existing_data, diff_df])
#         updated_data.to_csv('earthquakes.csv', index=False)
#         print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} New data appended to the CSV file.')
#     else:
#         print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} No new data found.')

# # ana döngü'de her 5 dakikada bir çalıştırma
# while True:
#     df = scrape_earthquake_data()
#     write_to_csv(df)
#     time.sleep(30)  # 5 dakika bekleme
#-------------------------------------------------------
# deprem verilerini dataframme'den alıp csv'ye yazma
def write_to_csv(df):
    # hali hazırda csv'deki verileri tekrar güncelleme sırasında okuma
    try:
        existing_data = pd.read_csv('earthquakes.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=df.columns)

    # yeni veriyi eskisi ile karşılaştırma
    # diff_df = df[~df.isin(existing_data)].dropna()
    # use a unique identifier for each earthquake instead of comparing all columns
    diff_df = df[~df['Date/Time'].isin(existing_data['Date/Time'])] # use 'Date/Time' instead of 'date_time'
    if not diff_df.empty:
        # yeni veri varsa csv'ye ekleme
        updated_data = pd.concat([diff_df, existing_data]) # reverse the order of arguments to prepend new data
        updated_data.to_csv('earthquakes.csv', index=False)
        print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} New data appended to the CSV file.')
    else:
        print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} No new data found.')

# ana döngü'de her 5 dakikada bir çalıştırma
while True:
    df = scrape_earthquake_data()
    write_to_csv(df)
    time.sleep(300)  # 5 dakika bekleme