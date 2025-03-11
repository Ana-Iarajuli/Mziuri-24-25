# nums = list()
# nums1 = []
# print(type(nums), type(nums1))
# nums1.append(2)
# print(nums1)

# texts = set()
# numbers = [1, 2, 1, 4, 123]
# texts1 = set(numbers)
# print(texts1)
# print(type(texts), type(texts1))


# my_set = {1,3,2}
# my_set.add(12.3)
# my_set.update([12,19], [212, "hello", False], "aksjdb", 12.3)
# print(my_set)
# for letter in "121!@$#.3":
#     if letter.isdigit():
#         print(letter)
# my_set.update([4,5], {1,6,8})
# print(my_set)

# my_set = {2, 4, 10}
# my_set.remove({2, 4})
# print(my_set)


# nums = {0, 1, 2, 3, 4}
# nums.update([5, 6, 7])
# nums.remove(0)
# nums.remove(1)
# for i in nums:
#     print(nums)

# my_set = {0, 1, 2, 3, 4}
# my_set.update([5, 6, 7])
# my_set.remove(2)
# my_set.remove(4)
#
# for element in my_set:
#     print(element)
#
# print(f"Number of elements in the set: {len(my_set)}")


set1 = {"green", "blue"}
set2 = {"blue", "yellow"}


union_method = set1.union(set2)
union_operator = set1 | set2

intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2

difference_method = set1.difference(set2)
difference_operator = set1 - set2

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print("Union (Method):", union_method)
print("Union (Operator):", symmetric_difference_operator)


user_input = input("Please enter a string: ")
unique_characters = set(user_input)

print("Unique characters in the string:")
for char in unique_characters:
    print(char)