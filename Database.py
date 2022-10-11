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

    def getpassword(self, id):
        try:
            insert = 'select "password" from "user" where "id" =' + "('%s')" % id
            self.cursor.execute(insert)
            rows = self.cursor.fetchall()
            self.db.commit()
            return rows[0][0]
        except Exception as e:
            print("DB err ", e)