import sqlite3
import datetime


class DB:
    def __init__(self, DB_name):
        self.DB_name = DB_name
        conn = sqlite3.connect(DB_name, check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class MessagesModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             time VARCHAR(20),
                             user_name VARCHAR(100),
                             type VARCHAR(100),
                             content VARCHAR(1000)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name='Anon', content='I love Mashas.', type='text'):
        time = str(datetime.datetime.now())
        time = time[:time.find('.')]
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO messages 
                          (time, user_name, type, content) 
                          VALUES (?,?,?,?)''', (time, user_name, type, content))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM messages WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM messages")
        rows = cursor.fetchall()
        return rows
