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


# how merge() fn works


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

    print(result)


# --------------O(1) constant--------
dict_from_list = {i: val for i, val in enumerate(arr)}

dict_from_list1 = {}
for i in range(len(arr)):
    dict_from_list1[i] = arr[i]

result1 = dict_from_list1
print(result1)
print(dict_from_list)
