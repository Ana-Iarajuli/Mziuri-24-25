# num = "1236754"
# for i in list(num):
#     print(i)
#
# double = [i*i for i in range(10)]
# print(double)
#
# cube = [i**3 for i in range(10) if i % 2 == 1]
# print(cube)
#
# l = [1, 2, 3, 4, 5]
# l_iter = iter(l)
# print(l_iter)
# print(l_iter.__next__())
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))

# მოცემულია სია [4, 5, 6, 7, 3, 5, 3, 1]. შექმენით სიის იტერატორი. next()
# ფუნქციის მეშვეობით წაიკითხეთ თითოეული ელემენტი და დაბეჭდეთ
# ეკრანზე. StopIteration შეცდომის გამოსროლის შემთხვევაში დაასრულეთ
# მონაცემების წაკითხვა.

# data = [4, 5, 6, 7, 3, 5, 3, 1]
# iterator = iter(data)
#
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break


# list = [4, 5, 6, 7, 3, 5, 3, 1]
# iter_list = iter(list)
# try:
#     for i in range(9):
#         print(next(iter_list))
# except StopIteration as e:
#     print(e)



# შექმენით სია, რომლის ელემენტებია 1-დან 100-მდე არსებული 5-ის ჯერადი რიცხვების კუბები.
# გამოიყენეთ for ციკლის მოკლე ჩაწერის ფორმა.
# შესაბამისი ფუნქციის გამოყენებით იპოვეთ სიის მაქსიმალური ელემენტი

# cubes = [i**3 for i in range(1, 100) if i % 5 == 0]
# print(min(cubes))
# print(cubes)


cube_list = [i ** 3 for i in range(1, 100) if i % 5 == 0]
print(cube_list)
print(f"maximum number {max(cube_list)}")