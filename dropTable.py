import sqlite3

# Connect to the SQLite database named 'ebookstore.db'
db = sqlite3.connect('ebookstore.db')

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Execute SQL command to drop the 'book' table and print a message confirming deletion of the 'book' table
cursor.execute('''DROP TABLE book''')
print('Book table deleted!')

# Commit  and close the database
db.commit()
db.close()

# Print a message confirming closure of the database connection
print('Connection to database closed')
