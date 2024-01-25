import mysql.connector


class Connector:
    """
    This class is responsible for connecting to MySQL Database.
    """
    def __init__(self):
        self._connection = None
        try:
            self._connection = mysql.connector.connect(host='35.180.109.183',
                                                       port='3306',
                                                       database='fiatalkaid',
                                                       user='nicro',
                                                       password='pwd',
                                                       )
            if self._connection.is_connected():
                pass
            #    print("Connected to MySQL Server!")

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL, ", e)

    def get_connection(self):
        """
        This method returns the connection to the MySQL database.
        :return: Connection instance.
        """
        return self._connection
