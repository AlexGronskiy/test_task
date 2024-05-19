"""
Завдання 5: Оптимізація алгоритмів
Напишіть функцію для сортування великого списку чисел за допомогою алгоритму злиття (merge sort)
і оцініть її продуктивність на списку з 1,000,000 випадкових чисел.
"""
import random
import time


def merge_sort(arr):
    """
    Сортує список чисел за допомогою алгоритму злиття.
    :param arr: список чисел
    :return: відсортований список
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    З'єднує дві частини списку в один відсортований список.
    :param left: ліва частина списку
    :param right: права частина списку
    :return: відсортований список
    """
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list


# Приклад використання та оцінка продуктивності:
random_list = [random.randint(0, 1000000) for i in range(1000000)]
start_time = time.time()
sorted_list = merge_sort(random_list)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")