"""
Завдання 1: Робота з базою даних
Напишіть функцію, яка підключається до бази даних SQLite,
створює таблицю `users` з полями `id`, `name`, `age`,
вставляє декілька записів і витягує всіх користувачів старших за певний вік.
"""

import sqlite3


def setup_database(db_name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    # Вставка записів
    users = [
        ('Alice', 30),
        ('Bob', 20),
        ('Charlie', 25),
        ('David', 35),
        ('Charlie2', 31),
        ('Charlie3', 27),
        ('Charlie4', 33)
    ]
    cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)

    # Збереження змін
    conn.commit()
    pass


def get_users_older_than(db_name, age):
    """
    Функція витягує всіх користувачів з бази даних старших за певний вік.
    :param db_name: назва бази даних
    :param age: вік
    :return: список користувачів
    """
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # Витягування всіх користувачів старших за певний вік
    cursor.execute('SELECT * FROM users WHERE age > ?', (age,))
    results = cursor.fetchall()

    # Закриття підключення
    conn.close()

    return results
    pass


# Приклад використання:
setup_database('test.db')
print(get_users_older_than('test.db', 30))  # Output: список користувачів старших за 30 років