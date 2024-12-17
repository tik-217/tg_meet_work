from config.db_connection import DB


class Vacancies(DB):
    def __init__(self):
        super().__init__()
        self.create_vacancies_table()

    def create_vacancies_table(self):
        # selection all vacancies
        self.cursor.execute(
            """--sql
        SELECT * FROM vacancies
        """
        )

        check_exist_table = self.cursor.fetchone()

        print(check_exist_table)

        if check_exist_table == None:
            self.cursor.execute(
                """--sql
            CREATE TABLE vacancies (id serial PRIMARY KEY, text varchar, user_id integer);
            """
            )

    def add_vacancy(self, text, user_id):
        self.cursor.execute(
            f"""--sql
        INSERT INTO vacancies (text, user_id) VALUES ('{text}', {user_id})
        """
        )

        self.connection.commit()
        # self.cursor.close()
        # self.connection.close()

    def get_vacancy(self, user_id):
        self.cursor.execute(
            f"""--sql
        SELECT * FROM vacancies WHERE user_id={user_id}
        """
        )

        return self.cursor.fetchone()


vacancies_instance = Vacancies()
vacancies_instance.add_vacancy("newasd", 1)
# vacancies_instance.create_vacancies_table()
# db.cursor.execute("INSERT INTO vacancies (text) VALUES ('new vacancy text')")

# db.cursor.execute("SELECT * FROM vacancies;")
# res = db.cursor.fetchone()

# print(res)

# db.connection.commit()

# db.cursor.close()
# db.connection.close()
