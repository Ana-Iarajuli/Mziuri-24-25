# filename = "davaleba1.txt"
# file1 = open(filename, 'r')
# file2 = open("students.txt", "w")
# file3 = open("davaleba1.txt", "r+")


filename = "food.txt"

# FILE
# file = open(filename, "r")
# food = file.read(9)
# print(food)
# file.close()

# FILE - WITH...AS
# with open(filename, "r", encoding="utf-8") as file:
#     content = file.read()
#
# print(content)


# with open(filename, "r", encoding="utf-8") as file:
#     line1 = file.readline(5)
#     line2 = file.readline(3)

# READLINE
# file = open(filename, "r", encoding="utf-8")
# food = file.readline(3)
# food2 = file.readline()
# # food3 = file.readline()
# print(food, food2)
# file.close()


# FOR LOOOP IN FILES
file = open(filename, "w", encoding="utf-8")
new_food = file.writelines("ჩურჩხელა")
# content = file.read()
# for line in file:
#     print(line)
