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

# -----------


arr = ["A", "B", "C"]
dict_from_list2 = {i: val for i, val in enumerate(arr)}
# print(dict_from_list2)

# -----------
