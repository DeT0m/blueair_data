#!usr/bin/env python3
import csv
import os
import sys
from datetime import datetime
import db_secrets
import database as db
import google_drive as gd


def migrate_gd_to_db(file_id_list, table):
    """
    Downloads data from Google Sheet and uploads it do database.
    Argumnent passed to this function must be a Google Drive
    file id inside a list
    Examples: file_id_list[-1:] or file_id_list[-2:]
    """
    for file in file_id_list:
        # Download file from Google Drive and save it as temporary .csv file
        drive.download_temp_file(file["id"])

        with open(drive.filename) as csv_file:  # Open temporary .csv file
            filereader = csv.reader(csv_file, delimiter=',')
            # Get the date of last query in database
            # Date is in first column
            last_query_date = con.get_last_date(table)[0]
            # Read data from row and save it in dictionary
            for row in filereader:
                if row[0] == '':  # Skip first row if it contains column titles
                    continue
                air_data = {
                    'date': datetime.strptime(row[0], '%B %d, %Y at %I:%M%p'),
                    'pm25': row[1],
                    'tvoc': row[2],
                    'co2':  row[3],
                    'temp': row[4],
                    'hum':  row[5],
                    }
                # If date in database is smaller than in file
                # or there is no record yet in database then
                # write row to database
                if (
                    (last_query_date is None)
                    or (last_query_date < air_data['date'])
                ):
                    print(f"Writing data from {air_data['date']}")
                    con.add_data(air_data, table)  # Write row data to database
        os.remove(drive.filename)  # Remove temporary file


FOLDER_ID = '1LYKq8vxWBQrS-nlUuAW_53Dtw86vzRS4'

os.chdir(os.path.dirname(sys.argv[0]))  # Change working directory
con = db.Connection(  # Connect to database
    db_secrets.DATABASE['host'],
    db_secrets.DATABASE['user'],
    db_secrets.DATABASE['passwd'],
    db_secrets.DATABASE['database'])
drive = gd.GoogleDriveSession(FOLDER_ID)  # Connect to Google Drive folder
file_list = drive.get_file_list()  # Get all files from folder
# Migrate data from Google Drive to database
migrate_gd_to_db(file_list[-2:], db_secrets.DATABASE['table'])
con.close_connection()  # Close connection with database
