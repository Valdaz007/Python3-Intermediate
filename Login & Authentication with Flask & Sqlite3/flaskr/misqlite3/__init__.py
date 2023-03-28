import sqlite3

class DB:
    def __init__(self, dbFile):
        self.dbFile = dbFile
        self.conxn = None
        self.cursor = None

    def open(self, dbFile):
        self.conxn = sqlite3.connect(self.dbFile)
        self.cursor = self.conxn.cursor()

    def close(self):
        self.conxn.close()

class Login(DB):
    def getUser(self, uname, upwd):
        self.open()
        self.cursor.execute(f"SELECT * FROM users WHERE uname = '{uname}' AND upwd = '{upwd}'")
        self.conxn.commit()
        results = self.cursor.fetchall()
        if len(results) >= 1:
            return True if results[0][3] == uname and results[0][4] == upwd else False
        else: return False

class SignUp(DB):
    pass
