from ast import arg
import sqlite3 as sq

class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.connection.execute('CREATE TABLE IF NOT EXISTS users(value_crypto TEXT, valutte TEXT, id_user INT)')
        self.connection.execute('CREATE TABLE IF NOT EXISTS time(time INT)')

    async def sql_read(self, select = '*', name_table = 'users'):
        with self.connection:
            try: 
                a = self.cursor.execute(f'SELECT {select} FROM {name_table}').fetchmany()
                return a
            except:
                print('Не найдено.')

    async def sql_quantity(self):
        with self.connection:
            return self.cursor.execute("SELECT count(*) FROM users").fetchone()
            

    async def sql_add_command(self, state):
        with self.connection:
            async with state.proxy() as data:
                a = tuple(data.values())
                self.cursor.execute(f'INSERT INTO users VALUES (?, ?, ?)', (a[0], a[1], a[2],))

    async def sql_upName(self, fname, tname, lname, id_user):
        with self.connection:
            self.cursor.executemany(f'UPDATE users SET Fname_user == ? WHERE id_user == ?', (fname, id_user,))
            self.cursor.executemany(f'UPDATE users SET Tname_user == ? WHERE id_user == ?', (tname, id_user,))
            self.cursor.executemany(f'UPDATE users SET Lname_user == ? WHERE id_user == ?', (lname, id_user,))

    async def sql_delete(self, id_user):
        with self.connection:
            self.cursor.executemany(f'DELETE FROM users WHERE id_user == ?', (id_user,))

SQL_DB = Database("users_time.db")