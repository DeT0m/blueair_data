import mysql.connector


class Connection():
    """Defining connection object"""

    def __init__(self, host, user, passwd, database):
        """
        Connects to database and creates cursor.
        Takes four string argument with database connection data
        """
        self.db = mysql.connector.connect(  # Connect to database
            host=host,
            user=user,
            passwd=passwd,
            database=database
            )
        self.cursor = self.db.cursor()  # Create cursor

    def add_data(self, data, table_name):
        """
        Adds data to database.
        Takes one dictionary argument with data and
        second argument with table name.
        """
        # Define table structure
        add_record = ("INSERT INTO %s " % (table_name) +
                      "(date, pm25, tvoc, co2, temp, hum) "
                      "VALUES (%(date)s, %(pm25)s, %(tvoc)s, %(co2)s,"
                      "%(temp)s, %(hum)s)")
        self.cursor.execute(add_record, data)
        self.db.commit()

    def get_last_date(self, table_name):
        """
        Gets last date from database.
        Takes one argument with table name.
        """
        query = ("SELECT date FROM %s " % (table_name) +
                 "ORDER BY date DESC LIMIT 1")
        self.cursor.execute(query)
        last_date = [None]
        for date in self.cursor:
            if date is None:
                pass
            else:
                last_date = date
        return last_date

    def close_connection(self):
        """Closes connection with database."""
        self.cursor.close()
        self.db.close()
