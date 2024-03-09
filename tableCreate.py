import sqlite3

# Connect to the SQLite database named 'ebookstore.db'
db = sqlite3.connect('ebookstore.db')

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Create a table named 'book' with columns: id, title, author, qty
cursor.execute('''
    CREATE TABLE book(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, 
    author TEXT, qty INTEGER)
''')

# Commit the transaction to save changes to the database
db.commit()
