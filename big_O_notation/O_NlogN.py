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
