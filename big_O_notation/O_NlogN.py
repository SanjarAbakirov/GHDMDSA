# ----O (N log N)----
import math
import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
# divide (log N) linear way
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
# via recursion sort both sides
    left = merge_sort(left)
    right = merge_sort(right)
# now act likely O(n)
    return merge_sort(left, right)


arr = [1, 4, 9, 5, 3, 8, 2, 1]

# how merge() fn works O(M log N)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            i += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # print(result)


# --------------O(1) constant--------
dict_from_list = {i: val for i, val in enumerate(arr)}

dict_from_list1 = {}
for i in range(len(arr)):
    dict_from_list1[i] = arr[i]

result1 = dict_from_list1
# print(result1)
# print(dict_from_list)

# ----O(1)----
students = ["ann", "boris", "victor", "galina"]
students_ids = {id: name for id, name in enumerate(students, start=100)}
# print(students_ids)

# ------O(1)----
goods = {"shues", "t-shorts", "throusers", "caps", "skirts"}
goods_ids = {id: item for id, item in enumerate(goods)}
# print(goods_ids)

# -----O(N log N)-------
arr = [45, 8, 91, 87, 1, 4, 2, 9, 7, 0, 3, 6]


def sort_and_merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # recurcion sort both sides
    left = sort_and_merge(left)  # 45, 8, 91, 87, 1, 4
    right = sort_and_merge(right)  # 2, 9, 7, 0, 3, 6
    return merge_arr(left, right)  # sort_and_merge([45], [8])


def merge_arr(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


sorted_arr = sort_and_merge(arr)
# print("original array", arr)
# print("sorted array", sorted_arr)

# --------------------
arr_pr = [35, 37, 90, 12, 34, 89, 25, 33]


def separator(arr_pr):
    if len(arr_pr) <= 1:
        return arr_pr
    mid = len(arr_pr)//2
    left = arr_pr[:mid]
    right = arr_pr[mid:]
    # recurcion sort both sides
    left = sort_and_merge(left)
    right = sort_and_merge(right)
    return merge_arr(left, right)


def sort_two_arr(left, right):
    result = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            b += 1
    result.extend(left[a:])
    result.extend(right[b:])

    return result


final = separator(arr_pr)
# sorted_arrs = sort_two_arr(arr_one, arr_two)
# print(f"Sorted array", final)

# ------------------big O notation ----- root complexity-----

# поиск всех делителей с коренвой сложностью


def find_divisions(n):
    # O(root n complexity)
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
def frind_divisors_optimized(n):
    # math.isqrt()
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


x = frind_divisors_optimized(49)
# print(x)


# --------------square complexity------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):  # if n = 5 than (0, 4)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
        return arr


numbers = [64, 34, 25, 12, 22, 11, 90]
# print("before sorting", numbers)
# print("after sorting", bubble_sort(numbers.copy()))

# -----------------square complexity--------


def selection_sort(arr):
    "at each staep seeking min"
    n = len(arr)
    for i in range(n):
        min_index = i  # preserve this value is minimum at this position
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


numbers = [64, 55, 82, 34, 25, 12, 22, 11, 90, 73]
# print("before sorting", numbers)
# print("after sorting", selection_sort(numbers.copy()))
