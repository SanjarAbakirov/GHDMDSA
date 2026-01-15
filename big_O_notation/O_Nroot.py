import math

# ------------------root n complexity-----
# поиск всех делителей с коренвой сложностью


def find_divisions(n):
    if n <= 0:
        return []
    divisors = []
    i = 1

    # iteration only from square num from n
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
# if divisors is not square root adding pare divisor
        i += 1

#  sort results
    divisors.sort()
    return divisors


# -----------

def find_divisors_optimized(n):
    math.isqrt(n)
    if n <= 0:
        return []

    divisors_1 = []
    sqrt_n = math.isqrt(n)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors_1.append(i)
            if i != n // i:
                divisors_1.append(n // i)

    divisors_1.sort()
    return divisors_1


x = find_divisors_optimized(49)
print(x)


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
