# O(N^2)

# нати все пары индексов (i, j) в массиве такие, что:
# 1. i < j
# 2. сумма элементов array[i] + array[j] равна заданному числу target

def find_pairs_bruteforce(arr, target):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # j всегда больше i
            if arr[i] + arr[j] == target:
                result.append((i, j))
    return result
