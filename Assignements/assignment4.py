# სავარჯიშო 2
# დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი
# რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. დაბეჭდეთ მიღებული შედეგი.

a = 1500
sum_a = 0

# while a <= 2100:
#     if a % 5 == 0 and a % 7 == 0:
#         print(a)
#         sum_a = sum_a + a
#     a = a + 1
#
# print(sum_a)




# დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის,
# 75, 80-ისა. გამოიყენეთ continue ოპერატორი.

# for num in range(15, 150):
#     if num % 5 == 0:
#         # if num == 50 or num == 75 or num == 80:
#         if num in (50, 75, 80):
#             continue
#         print(num)
#
#
#
# for num in range(15, 151):
#     if num % 5 != 0 or num == 50 or num == 75 or num == 80:
#         continue
#     print(num)




# factorial = 1
# number = int(input("Enter a number: "))
#
# for i in range(1, number + 1):
#     factorial *= i
#
# print(f"The factorial of {number}: {factorial}")



# a = int(input("Enter a number: "))
#
# factorial = 1
#
# if a < 0:
#     print("does not exist")
# elif a == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1, a + 1):
#         factorial = factorial * i
#     print("The factorial is", factorial)


# a = 1500
total = 0
#
# while a <= 2100:
#     if a % 5 == 0 and a % 7 == 0:
#         print(total)
#         if total > 20000:
#             break
#         total += a
#     a += 1
#
# print("ჯამი :", total)

# for a in range(1500, 2100, 5):
#     if total > 20000:
#         break
#     if a % 7 == 0:
#         total += a
# print(total)


total_sum = 0
for a in range(1500, 2101):
    if a % 5 == 0 and a % 7 == 0:
        if total_sum + a > 20000:
            break
        total_sum += a

print("Sum:", total_sum)