import mysql.connector as mysql

config = {
    'user':'st-onl',
    'passwd':'AVNS_tegPDkI5BlB2lW5eASC',
    'host':'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    'port':'25060',
    'database':'st-onl'
}

connection = mysql.connect(**config)
cursor = connection.cursor(dictionary=True)


cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolDB")
print("База данных SchoolDB создана (или уже существует).")

cursor.execute("USE SchoolDB")
print("Переключились на базу данных SchoolDB.")

create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(10) NOT NULL
)'''

cursor.execute(create_table_query)
print("Таблица students создана или уже существует.")


create_table_query = '''
CREATE TABLE IF NOT EXISTS rent_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    student_id INT,
    FOREIGN KEY (student_id)
        REFERENCES students (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
)'''

cursor.execute(create_table_query)
print("Таблица rent_books создана или уже существует.")

insert_values = [
    ('Nicolas', 'Shelekhov', 26, '20'),
    ('Petr', 'Bascow', 42, '6'),
    ('Vasiliy', 'Gretov', 19, '24'),
    ('Nicolay', 'Maslow', 35, '10')
]

create_table_query = 'INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)'
lst_id_list = []
for row in insert_values:
    cursor.execute(create_table_query, row)
    new_id = cursor.lastrowid
    lst_id_list.append(new_id)
print("Добавили запись в таблицу students")

create_table_query = 'INSERT INTO rent_books (title, student_id) VALUES (%s, %s)'

for i in lst_id_list:
    insert_values = ('default_name', i)
    cursor.execute(create_table_query, insert_values)

print("Добавили запись в таблицу rent_books")


connection.commit()



cursor.close()
connection.close()
