import datetime


# 1. Текущее время

date_now = datetime.datetime.now()
print(datetime.datetime.strftime(date_now,'%Y-%m-%d %H:%M:%S'))


# 2. Разница между датами
#    Создайте функцию, которая принимает две даты в формате YYYY-MM-DD и возвращает разницу между ними в днях.

def between_dates(date1, date2):
    form_date_1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    form_date_2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    def_between = form_date_1 - form_date_2
    if int(def_between.days) < 0:
        return abs(int(def_between.days))
    return def_between.days

date1 = "2024-10-08"
date2 = "2024-05-08"

print(between_dates(date1, date2))

# Добавление времени
'''
Добавление времени

Напишите программу, которая принимает от пользователя количество дней, часов, минут и секунд. 
Вычислите дату и время, которое будет через это количество времени от текущего момента.'''

user_input = input("Type date in format - days:hours:min:sec ")
user_days, user_hours, user_min, user_sec = user_input.split(":")
print(user_days, user_hours, user_min, user_sec)

delta = datetime.timedelta(days=int(user_days), hours=int(user_hours), minutes=int(user_min), seconds=int(user_sec))
print(f"Через {delta} будет - {datetime.datetime.now() + delta}")

# formated_user_date = datetime.datetime.strptime(user_date, "")