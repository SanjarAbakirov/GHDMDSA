
# --------------O(1) constant--------
dict_from_list = {i: val for i, val in enumerate(arr)}

dict_from_list1 = {}
for i in range(len(arr)):
    dict_from_list1[i] = arr[i]

result1 = dict_from_list1
# print(result1)
# print(dict_from_list)

# ----O(1)----
students = ["ann", "boris", "victor", "galina"]
students_ids = {id: name for id, name in enumerate(students, start=100)}
# print(students_ids)

# ------O(1)----
goods = {"shues", "t-shorts", "throusers", "caps", "skirts"}
goods_ids = {id: item for id, item in enumerate(goods)}
print(goods_ids)
