import sqlite3

class DB:
    def __init__(self):
        self.conxn = None
        self.cursor = None

    def open(self, dbFile):
        self.conxn = sqlite3.connect(dbFile)
        self.cursor = self.conxn.cursor()

    def close(self):
        self.conxn.close()

class Login(DB):
    def getUser(self, uname):
        self.cursor.execute(f"SELECT * FROM users WHERE uname = '{uname}'")
        self.conxn.commit()
        results = self.cursor.fetchall()[0]
        return results

class SignUp(DB):
    pass