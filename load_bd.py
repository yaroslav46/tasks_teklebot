import sqlite3

def load(name, org, date, locac):
    
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              org TEXT,
              date TEXT,
              locac TEXT)''')
    conn.commit()
    cur.execute(
        f"INSERT INTO users(name, org, date, locac) VALUES('{name}', '{org}', '{date}', '{locac}')"
    )
    conn.commit()
    cur.close()
    conn.close()