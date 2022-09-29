import sqlite3
from prettytable import PrettyTable


class DataManager:
    """
        Класс, отвечающий за менеджерение юзеров
        Основная цель - сейвить и апдейт языков перевода
    """

    def __init__(self, path):
        self.path = path

    def get_lang(self, id_user):
        """ Получить язык перевода """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()

        cur.execute("""SELECT * FROM users WHERE id = ?""", (id_user,))
        result = cur.fetchone()

        conn.close()
        return (result[2])  # lang юзера

    def create_user(self, name_user, id_user, lang_user, created_at):
        """ Создает нового юзера в таблице """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        user = (name_user, id_user, lang_user, created_at)

        # Проверка, находится ли юзер уже в базе
        # Если есть в базе - удаляет и перезаписывает
        cur.execute("""SELECT * FROM users WHERE id = ?""", (id_user,))
        if cur.fetchone() == None:
            cur.execute("""INSERT INTO users VALUES(?, ?, ?, ?);""", user)
            conn.commit()
        else:
            cur.execute("""DELETE FROM users WHERE id = ?""", (id_user,))
            cur.execute("""INSERT INTO users VALUES(?, ?, ?, ?);""", user)
            conn.commit()

        conn.close()
        print("USER create")

    def _show_table(self):
        """ Показывает таблицу юзеров """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        lines = cur.fetchall()

        table = PrettyTable()
        table.field_names = ["NANE", "ID", "LANG", "CREATED_AT"]
        for line in lines:
            table.add_row(line)

        print(table)
        conn.close()

    def _create_table(self):
        """ Проверяет файл .db, создает при отсутствии """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                        name TEXT, id TEXT, lang TEXT, created_at DATE);""")

        conn.commit()
        conn.close()
        print("DB is Update")

    def _clear_users(self):
        """ Очищает таблицу юзеров """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute("""DELETE FROM users;""", )
        conn.commit()
        conn.close()
        print("USERS Delete")
