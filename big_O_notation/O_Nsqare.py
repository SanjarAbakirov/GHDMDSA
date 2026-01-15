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
