
#  O(logN)
arr = [1, 2, 4, 5, 6, 7, 9]
index = bisect.bisect_left(arr, 5)
print(index)  # 3
