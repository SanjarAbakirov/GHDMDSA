
# --------------O(1) constant--------
arr = [23, 4, 5, 9, 1]
dict_from_list = {i: val for i, val in enumerate(arr)}

dict_from_list1 = {}
for i in range(len(arr)):
    dict_from_list1[i] = arr[i]

result1 = dict_from_list1
print(result1)
print(dict_from_list)

# ----O(1)----
students = ["ann", "boris", "victor", "galina"]
students_ids = {id: name for id, name in enumerate(students, start=100)}
print(students_ids)

# ------O(1)----
goods = {"shues", "t-shorts", "throusers", "caps", "skirts"}
goods_ids = {id: item for id, item in enumerate(goods)}
print(goods_ids)

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
