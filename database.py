import mysql.connector


class Connection():
    """Defining connection object"""

    def __init__(self):
        """Connects to database and creates cursor."""
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="demouser",
            passwd="demopassword",
            database="blueairdb"
            )
        self.cursor = self.db.cursor()

    def add_data(self, data):
        """Adds data to database."""
        add_record = ("INSERT INTO airdata "
                      "(date, pm25, tvoc, co2, temp, hum) "
                      "VALUES (%(date)s, %(pm25)s, %(tvoc)s, %(co2)s,"
                      "%(temp)s, %(hum)s)")
        self.cursor.execute(add_record, data)
        self.db.commit()

    def get_last_date(self):
        """Gets last date from database."""
        query = ("SELECT date FROM airdata "
                 "ORDER BY date DESC LIMIT 1")
        self.cursor.execute(query)

        for date in self.cursor:
            last_date = date
        return last_date

    def close_connection(self):
        """Closes connection with database."""
        self.cursor.close()
        self.db.close()
