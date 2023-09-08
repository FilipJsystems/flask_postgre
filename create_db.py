import psycopg2

# Połacz sie z baza PostgreSQL
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_db_user",
    password="your_password",
    host="localhost",
    port="5432"
)

# Tworzymy kursor do wykonywania kwerend SQL
cursor = conn.cursor()

# Twozymy tabelke ze zmiennymi: id, name, weight, height, and age
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id SERIAL PRIMARY KEY, name TEXT, weight FLOAT, height FLOAT, age INTEGER)''')

# Insertujemy dane do tabeli
users_data = [
    ('Filip', 68.5, 1.75, 25),
    ('Marcin', 72.5, 1.78, 30),
    # ... itd
]
cursor.executemany('INSERT INTO users (name, weight, height, age) VALUES (%s, %s, %s, %s)', users_data)

# zakomitowac trzeba w postrgres - nie ma autocommitu
conn.commit()

# zamykamy polaczenie
cursor.close()
conn.close()