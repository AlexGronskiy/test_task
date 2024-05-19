"""
Завдання 6: Використання логування
Напишіть програму, яка виконує кілька операцій з файлами і логуватиме всі події (наприклад,
відкриття файлу, читання даних, закриття файлу, помилки) з використанням стандартної бібліотеки `logging`.
"""
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("file_operations.log"),
                              logging.StreamHandler()])


def create_example_file_if_not_exists(f_path):
    """
    Створює файл з заданим шляхом і записує в нього деякий текст, якщо файл не існує.
    """
    try:
        # Спробуємо відкрити файл для читання
        with open(f_path, 'r') as file:
            logging.info(f"Файл {f_path} вже існує. Продовження роботи програми.")
    except FileNotFoundError:
        # Якщо файл не знайдено, створюємо його
        content = """
Деякий текст
Текст можно додати в будь який час відкрив example.txt
та прописав в ньому більше тексту.
Цей текст сгенерован автоматично як перший вхідний текст.
Кінець прикладу."""

        with open(f_path, 'w') as file:
            file.write(content)
        logging.info(f"Файл {f_path} створено з вмістом.")


def read_file(f_path):
    """
    Зчитує дані з файлу та логуватиме події.
    :param f_path: шлях до файлу
    :return: дані з файлу
    """
    try:
        logging.info(f"Відкриття файлу: {f_path}")
        with open(f_path, 'r') as file:
            data_f = file.read()
            logging.info(f"Читання даних з файлу: {f_path}")
        logging.info(f"Закриття файлу: {f_path}")
        return data_f
    except FileNotFoundError:
        logging.error(f"Файл не знайдено: {f_path}")
    except IOError as e:
        logging.error(f"Помилка вводу/виводу при роботі з файлом {f_path}: {e}")


# Приклад використання:
file_path = 'example.txt'
create_example_file_if_not_exists(file_path)
data = read_file(file_path)
if data is not None:
    print(data)
