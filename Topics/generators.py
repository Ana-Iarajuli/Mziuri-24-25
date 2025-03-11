# def my_gen():
#     n = 1
#     print(f"this is: {n}")
#     yield n
#     n += 4
#     print(f"this is: {n}")
#     yield n
#
#
# gen_var = my_gen()
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))


# შექმენით (აღწერეთ) 5-ის ჯერადი რიცხვების გენერატორი. გენერატორის
# მეშვეობით შექმენით იტერატორი და 10 ჯერ დაბეჭდეთ 5-ის ჯერადი
# რიცხვები თანმიმდევრობით.

# def multiples_of_five():
#     num = 5
#     while True:
#         yield num
#         num += 5
#
# iterator = multiples_of_five()
#
# count = 0
# while count < 10:
#     print(next(iterator))
#     count += 1


# def number_generator():
#     yield [1, 2, 3, 4, 5]
#
#
# iterator = iter(number_generator())
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
#
# nums = ["aleqsandre", 2, 3, 4, 5, "lazare"]
#         # 0  1  2  3  4  5
# print(nums[10]) # [index]

my_dict = {"name": "jasurbeki"}
char2 = "Babman"
my_tuple = (1, 2, 3, 4)
print(my_tuple[2])

print(char2.replace("B", "C"))

