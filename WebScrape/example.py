import sqlite3

# Establish connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#Query data
cursor.execute("SELECT * FROM events WHERE date = '2026.11.24'")
rows = cursor.fetchall()
print(rows)

# query certain columns
cursor.execute("SELECT band,date FROM events WHERE date = '2026.11.24'")
rows = cursor.fetchall()
print(rows)

#inserting new rows
new_rows = [('Baby Metal', 'LA', '2026.11.23'),
            ('Stereophonics', 'London', '2026.05.23')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

#print all
cursor.execute("SELECT * FROM events ")
rows = cursor.fetchall()
print(rows)



