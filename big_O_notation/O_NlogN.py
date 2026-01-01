# ----O (N log N)----
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
    left = sort_and_merge(left)  # 45, 8, 91, 87, 1, 4
    right = sort_and_merge(right)  # 2, 9, 7, 0, 3, 6
    return sort_and_merge(left, right)
