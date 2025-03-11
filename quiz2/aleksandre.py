#1

# for number in range(400, 99, -1):
#     if number % 9 == 0:
#         print(number)
# 13/15


#2
# list = [7,1,8,21,20]
# last_element = list[-1]
# print("სიის ბოლო ელემენტი:", last_element)
# 2.5/5

# # შედეგი:20
#
# #3
#
# def cube_list(numbers):
#     new_list = []
#     for a in numbers:
#         new_list.append(a**3)
#     return new_list
    # return [a**3 for a in numbers]

# numbers = [1, 2, 3, 4, 5]
# cubed_numbers = cube_list(numbers)
# print("ახალი სია:", cubed_numbers)
# 18/25
#
# # შედეგი: ახალი სია: [1, 8, 27, 64, 125]
#
#
#
# #5
#
# def favourite_fruit(fruit_list, favourite_fruit):
#     if favourite_fruit in fruit_list:
#         return fruit_list.index(favourite_fruit)
#     else:
#         return f"{favourite_fruit} არ არის სიაში."
#
#
# fruit_list = ['apple', 'banana', 'orange', 'grapes']
# user_favourite_fruit = input("რომელია შენი საყვარელი ხილი? ")
# result = favourite_fruit(fruit_list, user_favourite_fruit)
# #
# print(result)
# 15/30

# # შედეგი: რომელია შენი საყვარელი ხილი? orange
# # 1
# #        რომელია შენი საყვარელი ხილი? watermelon
# # watermelon არ არის სიაში.
# #
# # ბონუს დავალება
#
# #3
from math import pow
result = pow(5, 4)

print(result)
# 5/10
# შედეგი:625

