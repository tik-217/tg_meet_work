import psycopg2


class DB:
    "DB connection"

    def __init__(self):
        self.connection = psycopg2.connect(
            "dbname=template1 user=postgres password=root port=5434"
        )

        self.cursor = self.connection.cursor()
