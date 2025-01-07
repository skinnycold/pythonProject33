import mysql.connector as mysql

# Подключение к БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl'
)
#
# # Создание курсора
# cursor = db.cursor(dictionary=True)
#
#
# cursor.execute("SELECT * FROM students")
# print(cursor.fetchall())

db.close()