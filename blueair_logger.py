import os
from datetime import datetime
import csv
import database as db
import google_drive as gd

os.chdir(os.path.abspath('.'))  # Change working directory

con = db.Connection()

with open('temp.csv') as csv_file:
    filereader = csv.reader(csv_file, delimiter=',')
    last_query_date = con.get_last_date()[0]
    for row in filereader:
        air_data = {
            'date': datetime.strptime(row[0], '%B %d, %Y at %I:%M%p'),
            'pm25': row[1],
            'tvoc': row[2],
            'co2':  row[3],
            'temp': row[4],
            'hum':  row[5],
            }
        if last_query_date < air_data['date']:
            print(f"Data: {air_data['date']}\n"
                  f"PM 2.5: {air_data['pm25']}\n"
                  f"tVOC:{air_data['tvoc']}\n"
                  f"CO2: {air_data['co2']}\n"
                  f"Temperatura: {air_data['temp']}\n"
                  f"Wilgotność: {air_data['hum']}")
            # con.add_data(air_data)

con.close_connection()
# os.remove('temp.csv')  # Remove temporary file

# TODO: Upload do bazy danych wszystkich dotychczasowych rekordów
# for file in os.listdir('./data'):
#     print(file)

# TODO: uruchomienie automatycznego uploadu dla najnowszych rekordów
