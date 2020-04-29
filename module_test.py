import database as db
import google_drive as gd
from datetime import datetime

FOLDER_ID = '1LYKq8vxWBQrS-nlUuAW_53Dtw86vzRS4'

today = datetime.now()

# con = db.Connection()

air_data = {
        'date': today,
        'pm25': 16.63,
        'tvoc': 437,
        'co2': 1850,
        'temp': 29.92,
        'hum': 50.44,
    }

# con.add_data(air_data)

# print(con.get_last_date())

drive = gd.GoogleDriveSession(FOLDER_ID)
file_list = drive.get_file_list()
drive.download_temp_file(file_list[0]["id"])
