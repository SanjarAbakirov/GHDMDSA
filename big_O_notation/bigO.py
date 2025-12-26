# arr = [7, 4, 9, 5, 3, 8, 2, 1]
# print("cheking", arr)
# for i in range(len(arr)):
#     for j in range(len(arr) - 1 - i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print("enhanced arr", arr)

# ------------------
# O(1) constant & complicate
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# first_element = my_list[0]
# middle_element = my_list[5]
# last_element = my_list[-1]
# print(first_element)
# print(middle_element)
# print(last_element)

# -----------------
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list)

# last_element = my_list.pop()
# print(my_list)

# my_list.insert(0, 0)
# my_list.pop(0)
# print(my_list)
# ---------------

my_dict = {'apple': 5, 'banana': 10, 'orange': 7}
my_set = {1, 2, 3, 4, 5}
# O(1) in average case
my_dict['grape'] = 15  # insert
value = my_dict['apple']  # receiving 5
exists = 'banana' in my_dict
print(my_dict)
