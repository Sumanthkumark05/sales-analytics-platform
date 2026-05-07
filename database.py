import sqlite3

connection = sqlite3.connect('sales.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    sales INTEGER
)
''')

connection.commit()
connection.close()