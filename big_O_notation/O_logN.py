import math
import bisect
#  O(logN)
arr = [1, 2, 4, 5, 6, 7, 9]
index = bisect.bisect_left(arr, 5)
print(index)  # 3


arr2 = [7, 4, 9, 5, 3, 8, 2, 1]
print("cheking", arr2)
for i in range(len(arr2)):
    for j in range(len(arr2) - 1 - i):
        if arr2[j] > arr2[j + 1]:
            arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
print("enhanced arr", arr2)
