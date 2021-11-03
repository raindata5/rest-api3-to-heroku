import sqlite3

conn = sqlite3.connect('flask-languages.db')
cursor = conn.cursor()

# creating the User table
table_query = 'create table User (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(table_query)

# creating the Language table
table_query2 = 'create table Language (id INTEGER PRIMARY KEY, name text, country text);'
cursor.execute(table_query2)

# test
# cursor.execute('insert into Language values ("russe", "russie");')
# cursor.execute('select * from Language')
# result = cursor.fetchall()
# print(result)
conn.commit()
conn.close()
