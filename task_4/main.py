"""
Завдання 4: Робота з веб-фреймворками
Напишіть простий RESTful API за допомогою Flask, який має два ендпоїнти:
один для додавання нового користувача і один для отримання списку всіх користувачів
"""
from flask import Flask, request, jsonify
app = Flask(__name__)
users = [{"name": "John", "age": 30}]


@app.route('/users', methods=['POST'])
def add_user():
    """
    Додає нового користувача.
    """
    user = request.get_json()
    if 'name' in user and 'age' in user:
        users.append(user)
        return jsonify(user), 201
    else:
        return jsonify({"error": "Invalid input"}), 400


@app.route('/users', methods=['GET'])
def get_users():
    """
    Повертає список всіх користувачів.
    """
    return jsonify(users), 200


if __name__ == '__main__':
    app.run(debug=True)
# Приклад використання:
# POST /users з даними {"name": "John", "age": 30}
# GET /users повертає список всіх користувачів