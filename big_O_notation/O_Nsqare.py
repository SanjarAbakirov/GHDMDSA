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
print("before sorting", numbers)
print("after sorting", selection_sort(numbers.copy()))


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


# ----- square complexity -------


# def find_all_divisors(n: int) -> list:
#     """Нахождение всех делителей числа за O(√n)"""
#     divisors = []

#     # Идем только до √n
#     for i in range(1, int(math.isqrt(n)) + 1):  # for i in range(1, 7)
#         if n % i == 0:
#             divisors.append(i)
#             # Добавляем парный делитель (кроме случая i = n/i)
#             if i != n // i:
#                 divisors.append(n // i)

#     return sorted(divisors)


# # Пример
# print(find_all_divisors(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
# print(find_all_divisors(17))  # [1, 17]
