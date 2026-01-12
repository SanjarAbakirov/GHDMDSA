# arr = [7, 4, 9, 5, 3, 8, 2, 1]
# print("cheking", arr)
# for i in range(len(arr)):
#     for j in range(len(arr) - 1 - i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print("enhanced arr", arr)

# ------------------
# O(1) constant & complicate
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# first_element = my_list[0]
# middle_element = my_list[5]
# last_element = my_list[-1]
# print(first_element)
# print(middle_element)
# print(last_element)

# -----------------
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list)

# last_element = my_list.pop()
# print(my_list)

# my_list.insert(0, 0)
# my_list.pop(0)
# print(my_list)
# ---------------

import math
import bisect
my_dict = {'apple': 5, 'banana': 10, 'orange': 7}
my_set = {1, 2, 3, 4, 5}
# O(1) in average case
my_dict['grape'] = 15  # insert
value = my_dict['apple']  # receiving 5
exists = 'banana' in my_dict

# print(my_dict)

my_set.add(6)  # insert
exists = 3 in my_set
# print(my_set)
# print(my_dict)


#  O(logN)
arr = [1, 2, 4, 5, 6, 7, 9]
index = bisect.bisect_left(arr, 5)
# print(index)  # 3

# -------------


# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / power(x, -n)
#     if n % 2 == 0:
#         half = power(x, n // 2)
#         return half * half
#     else:
#         return x * power(x, n - 1)


# print(power(2, 10))  # 1024

# ---binary search---------------
def binary_search2(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# example & pattern of useage
arr = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search2(arr, 7))  # 3
# print(binary_search2(arr, 10))  # -1

# -----------O(N)
# example:

# dict_from_list = {i: val for i, val in enumerate(arr)}
# dict_from_list1 = {}
# for i in range(len(arr)):
#     dict_from_list1[i] = arr[i]


# --------
arr = ["A", "B", "C"]
dict_from_list2 = {i: val for i, val in enumerate(arr)}
# print(dict_from_list2)

# -----------O(N)----


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 7)
# print(a)


# ----- quadratic complexity -------


def find_all_divisors(n: int) -> list:
    """Нахождение всех делителей числа за O(√n)"""
    divisors = []

    # Идем только до √n
    for i in range(1, int(math.isqrt(n)) + 1):  # for i in range(1, 7)
        if n % i == 0:
            divisors.append(i)
            # Добавляем парный делитель (кроме случая i = n/i)
            if i != n // i:
                divisors.append(n // i)

    return sorted(divisors)


# Пример
print(find_all_divisors(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(find_all_divisors(17))  # [1, 17]
# --------------------------------------
# Two Sum (LeetCode #1)
# Условие:
# Дан массив целых чисел nums и целое число target. Верните индексы двух чисел, сумма которых равна target.
# Можно считать, что для каждого входного массива существует ровно одно решение.
# Нельзя использовать один и тот же элемент дважды.
# Ответ можно вернуть в любом порядке.
# -------------Brute Force-arr-----------


def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# -----hastag table------

def twoSum(nums, target):
    hashmap = {}  # Значение: индекс
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:  # Проверка занимает O(1) в среднем
            return [hashmap[complement], i]
        hashmap[num] = i

# -------------------
# Input: n = 10
# Output: 4  # Простые числа меньше 10: 2, 3, 5, 7

# slow


def countPrimes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, x):  # Проверка всех делителей
            if x % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

# fast


def countPrimes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):  # Ключевое изменение!
            if x % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count


# Условие:
# Дан массив целых чисел nums и целое число target. Верните индексы двух чисел, сумма которых равна target.

# Можно считать, что для каждого входного массива существует ровно одно решение.
# Нельзя использовать один и тот же элемент дважды.
# Ответ можно вернуть в любом порядке.
# Пример:

# python
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  # Потому что nums[0] + nums[1] = 2 + 7 = 9
# Решение 1: Brute Force(Полный перебор)

# python


def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# Анализ Big O:

# Время: O(n²). Два вложенных цикла. В худшем случае для каждого из n элементов мы перебираем почти все остальные(n-1, n-2, ...). Это n*(n-1)/2 операций → O(n²).
# Память: O(1). Мы не используем дополнительных структур данных, кроме нескольких переменных.
# Решение 2: Хэш-таблица(Оптимальное)

# python


def twoSum(nums, target):
    hashmap = {}  # Значение: индекс
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:  # Проверка занимает O(1) в среднем
            return [hashmap[complement], i]
        hashmap[num] = i


# Анализ Big O:

# Время: O(n). Один проход по массиву из n элементов. Поиск в словаре(if complement in hashmap) в среднем занимает O(1).
# Память: O(n). В худшем случае мы сохраним в хэш-таблице почти все n элементов(если ответ будет в конце массива).
# Сравнение на практике:

# Представим n = 10, 000:

# O(n²): ~ 50, 000, 000 операций(это много, может быть медленно).
# O(n): ~ 10, 000 операций(быстро).
# Как аргументировать Big O на собеседовании(структура ответа):

# Опишите алгоритм: «Я использую хэш-таблицу для хранения пройденных чисел и их индексов».
# Обоснуйте сложность по времени:

# «Мы проходим по массиву один раз — это O(n)».
# «На каждой итерации мы делаем поиск и вставку в хэш-таблицу, что в среднем занимает O(1)».
# Итог: O(n) * O(1) = O(n).
# Обоснуйте сложность по памяти:

# «В худшем случае мы храним n-1 элемент в хэш-таблице, прежде чем найдём пару».
# Итог: O(n).
# Сравните с brute-force: «Это лучше, чем O(n²) по времени, но требует дополнительной памяти O(n) против O(1) у brute-force. Это классический trade-off».
# Другие классические примеры Big O на LeetCode:

# Binary Search(Задача 704): O(log n) — массив постоянно делится пополам.
# Merge Sort / Quick Sort(Задачи на сортировку): O(n log n) — стандартная сложность для сравнимых сортировок.
# Traversing a Matrix(Задачи с 2D grid): O(m * n), где m — строки, n — столбцы.
# Subsets / Combinations(Задача 78): O(2 ^ n) — экспоненциальный рост, так как нужно рассмотреть все подмножества.
# Fibonacci Recursive(наивная реализация): O(2 ^ n) — множество повторных вычислений.
# Three Sum(Задача 15): Оптимальное решение за O(n²) — часто это следующий шаг после Two Sum.
# Ключевой вывод:

    # Условие:
    # Дано целое число n. Верните количество простых чисел, которые меньше n.

    # Пример:

    # python
    # Input: n=10
    # Output: 4  # Простые числа меньше 10: 2, 3, 5, 7
    # Решение 1: Brute Force(Naïve) - O(n√n)

    # python


def countPrimes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, x):  # Проверка всех делителей
            if x % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

# Сложность: O(n²) - очень медленно.
# Решение 2: Улучшенная проверка - O(n√n)

# python


def countPrimes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):  # Ключевое изменение!
            if x % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

# Откуда здесь O(√n)?
# При проверке числа x на простоту нам не нужно проверять все делители до x:
# Если x не простое, то его можно представить как x = a * b
# Один из множителей (пусть a) будет ≤ √x
# Поэтому достаточно проверить делители только до √x
# Анализ сложности:
# Проверка одного числа: O(√x)
# Для всех чисел до n: O(∑ √x) для x от 2 до n
# Это примерно O(n√n) в целом


# ---------------------

def search(nums, target):
    """
    Реализация бинарного поиска с логарифмической сложностью O(log n)
    Args:
        nums: отсортированный список целых чисел
        target: искомое значение
    Returns:
        Индекс target или -1 если не найден
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        # Находим средний индекс
        mid = left + (right - left) // 2  # Предотвращает переполнение

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример использования
if __name__ == "__main__":
    # Тест 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Массив: {nums1}")
    print(f"Индекс {target1}: {search(nums1, target1)}")  # Output: 4

    # Тест 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"\nМассив: {nums2}")
    print(f"Индекс {target2}: {search(nums2, target2)}")  # Output: -1
