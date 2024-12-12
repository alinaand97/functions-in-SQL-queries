# Выбор элементов и функции в SQL запросах


import sqlite3

# Подключение к базе данных not_telegram.db
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


# Удаление записи с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')
connection.commit()

# Подсчёт всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисление и вывод среднего баланса
if total_users > 0:
    average_balance = all_balances / total_users
    print(average_balance)
else:
    print('Нет пользователей для расчета')

# Закрытие соединения с базой данных
connection.close()