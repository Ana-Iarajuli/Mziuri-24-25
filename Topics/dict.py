# my_dict = {
#     "name": "keti",
#     "age": 40,
#     "children": [{"name": "ana", "age": 15},
#                  {"name": "toko", "age": 80}]
# }
# print(my_dict)


# students = {'Nica': 'A', 'Luka': 'B', 'Nika': 'A', "John": 10}
# # print(students['John'])
# # print(students.get("John", "ეს სახელი ლექსიკონში არ მოიძებნა"))
# students["Luk"] = "A"
# print(students)

# squares = {3: 9, 5: 25, 7: 49, 9: 81, 1: 1}
# del squares[7]
# squares.pop(3)
# # squares.clear()
# print(squares)
# print(sorted(squares))



person = {
            "firstName": "Jane",
            "lastName": "Doe",
            "hobbies": ["running", "sky diving", "singing"],
            "age": 35,
            "children": [
                {
                    "firstName": "Alice",
                    "age": 6
                },
                {
                    "firstName": "Bob",
                    "age": 8
                }
            ]
        }
# print()person["children"]
# children2 = person.get('ksajbdjs', "jasurbeki")
# print(children2)
# print(person["lastName"])
# print(person.get("lastNam", "gvari shegeshala dzmobilo"))
# child_name1 = children[0]["firstName"]
# child_name2 = children[1]["firstName"]
# print(child_name1, child_name2)
# print("Children Names:", ", ".join(child["firstName"] for child in children))
#
# for child in children:
#     print(child["firstName"])


# text = "ragaca ragaca davigale agar minda gakvetilze"
# print(text)
# list1 = text.split()
# list2 = ['ragaca', 'ragaca', 'davigale', 'agar', 'minda', 'gakvetilze']
# text = ", ".join(list2)
# print(text)


# squares = {1: 1, 9: 81, 3: 9, 7: 49}
# print(sorted(squares))


squares = {1: 1, 9: 81, 3: 9, 7: 49}
print(squares.get(33, "nametania"))
# new_dict = squares.copy()
# new_dict_2 = squares.fromkeys({1, 3, 7, 9})
# print(new_dict_2)
#
# dict1 = {
#     'საჭმელი': {'ხინკალი': 99, 'ხაში': 0},
#      8: 16
# }
# print(dict1)

squares_list = squares.fromkeys(["12", "13"], "jirafi")
print(squares_list)
# print(squares_list[1])

# for key in squares.values():
#     print(key)
