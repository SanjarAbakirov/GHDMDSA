def merge_sort(arr):
    if len(arr) <= 1:
        return arr
# divide (log N) linear way
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
