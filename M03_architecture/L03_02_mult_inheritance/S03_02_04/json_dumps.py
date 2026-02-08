import json

my_dict = {"name": "Alice", "age": 30}
json_string = json.dumps(my_dict, ensure_ascii=False, indent=4)
print(json_string)
# Вывод:
# {
#     "name": "Alice",
#     "age": 30
# }