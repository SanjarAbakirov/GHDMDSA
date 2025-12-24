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


# параллели
if __name__ == "__main__":
    numbers = [2, 7, 11, 15, 3, 6, 8]
    target_sum = 10

    print("Array:", numbers)
    print("Target sum:", target_sum)

    pairs = find_pairs_bruteforce(numbers, target_sum)

    print("\nFound pairs (index):")
    for i, j in pairs:
        print(
            f" ({i}, {j}): {numbers[i]} + {numbers[j]} = {numbers[i] + numbers[j]}")

    print("\nAlternative input (values):")
    for i, j in pairs:
        print(f" {numbers[i]} + {numbers[j]} = {target_sum}")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# bubble sort example
if __name__ == "__main__":
    print("\n" + "="*50)
    print("bubble sort exapmle")

    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Before sorting:", unsorted_array)

    sorted_array = bubble_sort(unsorted_array.copy())
    print("Sort field:", sorted_array)
