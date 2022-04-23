from .database_connector import DatabaseConnection

class DatabaseRepository:

    @classmethod
    def insert_artist(cls, data):
        query = '''
            INSERT INTO artists
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        '''

        cursor = DatabaseConnection.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnection.connection.commit()
