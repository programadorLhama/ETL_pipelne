import mysql.connector as mysql

class DatabaseConnection:
    def __init__(self) -> None:
        self.connection = None

    def connect(self):
        db_connection = mysql.connect(
            host = "localhost",
            port = 3300,
            user = "root",
            passwd = "my-pw"
        )
        self.connection = db_connection
