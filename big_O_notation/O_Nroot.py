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
