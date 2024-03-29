from db import DBConnection
import datetime

class UserCRUD:
    table_name = 'users'

    def get(self, db, field: str):
        sql = "SELECT * FROM users WHERE username = ?;"
        user = db.cursor.execute(sql, (field, )).fetchone()
        return user # (id, username)

    def get_all(self, db):
        sql = "SELECT * FROM users;"
        users = db.cursor.execute(sql).fetchall()
        return users

    def update(self, db, field, value):
        pass

    def delete(self, db, field):
        pass

    def __check_user(self, db, value):
        sql = "SELECT id FROM users WHERE username = ?;"
        user_id = db.cursor.execute(sql, (value,)).fetchone()
        return False if not user_id else True

    def create(self, db: DBConnection, value):
        sql = "INSERT INTO {table_name}(username) VALUES(?)"
        if not self.__check_user(db, value):
            db.cursor.execute(sql.format(table_name=self.table_name), (value,))
            db.connection.commit()
            user = self.get(db, value) # получаем нового пользователя
            return user
            # print('добавили пользователя', value)

        return "Пользователь с таким username уже есть!"

