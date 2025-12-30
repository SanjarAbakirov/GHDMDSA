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

# import bisect
# my_dict = {'apple': 5, 'banana': 10, 'orange': 7}
# my_set = {1, 2, 3, 4, 5}
# # O(1) in average case
# my_dict['grape'] = 15  # insert
# value = my_dict['apple']  # receiving 5
# exists = 'banana' in my_dict

# print(my_dict)

# my_set.add(6)  # insert
# exists = 3 in my_set
# # print(my_set)
# print(my_dict)


#  O(logN)
arr = [1, 2, 4, 5, 6, 7, 9]
index = bisect.bisect_left(arr, 5)
print(index)  # 3

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
print(binary_search2(arr, 7))  # 3
print(binary_search2(arr, 10))  # -1

# -----------O(N)
# example:

# dict_from_list = {i: val for i, val in enumerate(arr)}
# dict_from_list1 = {}
# for i in range(len(arr)):
#     dict_from_list1[i] = arr[i]


# --------
arr = ["A", "B", "C"]
dict_from_list2 = {i: val for i, val in enumerate(arr)}
print(dict_from_list2)

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
print(a)
