
import psycopg2

connection = psycopg2.connect(
    database="library_api",
    user="app",
    password="Testing1",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()