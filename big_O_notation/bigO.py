arr = [7, 4, 9, 5, 3, 8, 2, 1]
print("cheking": arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("enhanced arr", arr)
