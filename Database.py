"""
This is the database
"""
import psycopg2


class Database:
    def __init__(self):
        try:
            self.db = psycopg2.connect(
                host="localhost",
                database="study",
                user="postgres",
                password="hyun0421")
        except Exception as e:
            print("DB err ", e)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def sign_up(self, id, password):
        try:
            insert = 'insert into "user" values (' + "'%s', '%s')" % (id, password)
            self.cursor.execute(insert)
            self.db.commit()
            return True
        except Exception as e:
            return False

    def getpassword(self, id):
        try:
            insert = 'select "p" from "user" where "u" =' + "('%s')" % id
            self.cursor.execute(insert)
            rows = self.cursor.fetchall()
            self.db.commit()
            return rows[0][0]
        except Exception as e:
            print("DB err ", e)
            return None