"""
Завдання 2: Написання тестів
Напишіть тести для функції, яка перевіряє, чи є рядок паліндромом.
Використовуйте бібліотеку `unittest`.
"""
import unittest
# Палиндро́м — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101;
# слова «топот» в русском языке и фин. saippuakivikauppias (продавец мыльного камня; торговец стеатитом) — самое
# длинное слово-палиндром в мире; текст «а роза упала на лапу Азора» и прочие являются палиндромами.
# Дата 22 февраля 2022 года тоже является палиндромом


def is_palindrome(s):
    """
    Функція перевіряє, чи є рядок паліндромом.
    :param s: рядок
    :return: True, якщо рядок паліндром, інакше False
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("Python"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("Noon"))
        self.assertTrue(is_palindrome("Civic"))

    def test_with_special_characters(self):
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertTrue(is_palindrome("Able , was I saw eLba"))


# Запуск тестів
if __name__ == '__main__':
    unittest.main()