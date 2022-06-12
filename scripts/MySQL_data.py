import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect("users_time.db")
    cur = base.cursor()
    if base:
        print('Data base connected OK! ')
    base.execute('CREATE TABLE IF NOT EXISTS users(value_crypto TEXT, valutte TEXT, id_user INT)')
    base.commit()

async def sql_read():
    try: 
        a = cur.execute(f'SELECT * FROM users').fetchmany()
        return a
    except:
        print('Не найдено.')


async def sql_add_command(state):
    async with state.proxy() as data:
        a = tuple(data.values())
        cur.execute(f'INSERT INTO users VALUES (?, ?, ?)', (a[0], a[1], a[2]))
        base.commit()

async def sql_upName(fname, tname, lname, id_user):
    cur.execute(f'UPDATE users SET Fname_user == ? WHERE id_user == ?', (fname, id_user,))
    cur.execute(f'UPDATE users SET Tname_user == ? WHERE id_user == ?', (tname, id_user,))
    cur.execute(f'UPDATE users SET Lname_user == ? WHERE id_user == ?', (lname, id_user,))
    base.commit()


async def sql_delete(id_user):
    cur.execute(f'DELETE FROM users WHERE id_user == ?', (id_user,))
    base.commit()