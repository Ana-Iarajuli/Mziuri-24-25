# # number = "5"
# # a = False
# # name = "Nikoloz "
# # surname = 'Pavliashvili'
# # num = "True"
# #
# # name_surname = name + surname
# #
# # print(float(number))
# # # print(type(a))
# # # print(type(name))
# # print(name_surname)
#
# # num1 = 15 ** 4
# # num2 = pow(15, 4, 2)
# #
# # num3 = abs(-10)
# #
# # print(num1)
# # print(num2)
# # print(num3)
#
# # x = 17
# # print(hex(x))
#
#
# """
# me vprintav dzaxilis nishans ricxviti mnishvnelobit
# print(chr(33))
# """
#
#
# # age = input("Enter your age: ")
# # print("Age:", age)
#
# # num1 = int(input("Enter num1: "))
# # num2 = int(input("Enter num2: "))
# # print(num1 + num2)
# # print(type(num1))
#
#
#
#
# # x = 3
# # y = 1
# # m = 7
# # print(min(x, y, m))
# # if max(x, y, m) == m:
# #     print("m is max")
#
#
# # x = 3
# # y = 1
# # #a
# # if x > y:
# #     print("x metia")
# # elif x < y: #შემოდის მხოლოდ მაშინ როდესაც if არის False
# #     print("x naklebia")
# # else:
# #     print("tolia")
# #
# #
# # if x == y:
# #     print("x tolia y-is")
# # else:
# #     if x > y:
# #         print("x metia")
# #     else:
# #         print("x naklebia")
# #
# # #b
# # if x > y:
# #     print("x metia")
# #
# # if x < y:
# #     print("x naklebia")
# # else:
# #     print("tolia")
#
#
#
#
# # a = 1
# #
# # while a <= 10:
# #     a += 1
# #     if a == 8:
# #         continue
# #     print(a)
#
#
#
# # for m in range(1, 11):
# #     print(m)
# #     if m == 8:
# #         break
#
# # name = "jasurbek"
# # surname = "iaxshiboevi"
# # print("სახელი: ", name, " გვარი: ", surname, " სახელი-გვარი:", name, " ", surname, sep='')
# # # print("გვარი:", surname)
#
# # name = 'Alice'
# # a = 5
# # print("Hi %s, I have %d donuts" %(name, a))
#
#
# # a = 5.3
# # print(int(a))
# # print('%d' %a) # arafers
# # print('%4d' %a) # arafers
# # print('%f' %a) # 5.3 || 5
# # print('%.2f' %a) # 5.3 || 5.30
#
# # name = 'Alice'
# # a = 5
# # print("Hi %s, I have %d donuts" %(name, a))
#
# # fname="John"
# # age=36
# # fsurname="xvichia"
# #
# # txt1 = "My name is {}, My surname is {}, I'm {}".format(fname, fsurname, age)
# # print(txt1)
# # txt2 = "My name is {0}, I'm {1}, i love {2}".format(36, "John", "eating")
# # print(txt2)
# # txt3 = "My name is {}, I'm {}, {}".format("John", 36, "aljbdfad")
# # print(txt3)
#
# # print(f"My name is {fname}, My surname is {fsurname}, I'm {age}")
#
#
#
#
#
#
# # both = name + surname
# # print(name, surname, name, name, surname, sep="@")
# # print(name, name, sep="_", end='\t')
# # print(surname)
#
#
#
#
# #davaleba1
# # a = 8
# # b = 5
# # c = a * 2 + b * 2
# # print(c)
#
# #davaleba2
# # a = int(input("enter a num: "))
# #
# # for i in range(2, a):
# #
# #
# #     print("not prime")
# #     break
# # else:
# #     print("Prime")
#
# #davaleba3
# # a = 1
# # sum = 0
# # while a <= 40:
# #     if a % 2 == 0:
# #         sum = sum + 1
# #     i = i + 1
# # print("Sum =", sum)
#
# # #davaleba4
# # a = 1
# # while a < 100:
# #     if a % 5 == 0:
# #         break
# #     a += 1
# #
# # print(a)
#
# #davaleba5
#
# for i in range(1, 31):
#     if i % 2 != 0:
#         continue
#     print(i)
#     i += 1
#
# #davaleba6
# a = int(input("enter a num: "))
# b = int(input("enter a second num: "))
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("they are equal")
#
#
#
# #bonus1
# #if cikli aris piroba romelic mowmdeba da tu martalia shesabamis pasuxs izleva
# #elif gamoiyeneba tu meore pirobis chawera gvsurs
# #else gamoiyeneba rom dagvibrunos pasuxi tu is arcerts arc ifs da arc ekifs ar akmayofilebs
#
# # a = 1
# # b = 2
# # if a > b:
# # print(a)
# # elif b > a:
# # print(b)
# # else:
# # print("gg")
#
#
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
#
#
#
#
# list = []
# a = int(input("enter number:"))
# raodenoba = 0
# while a > 0:
#     list.append(a % 10)
#     a= a // 10
#     raodenoba +=1
# print(raodenoba)
# print(list)
#
#


# num = int(input("enter a number: "))
# count = 0
# reversed = ""
#
# while num != 0:
#     last_num = num % 10 # 3; 2; 1
#     reversed += str(last_num)
#     print("floor is", num // 10)
#     num = num // 10
#     count += 1
#
# print(count)
# print(reversed)


# a = input("num 1: ")
# b = input("num 2: ")
# c = a + b
# print(c)



# def output_name(name1):
#     return f"გამარჯობა {name1}"
#
#
# name = input("Enter your name: ")
# print(output_name(name))


# def even_number(number):
#     """
#     ნაშთიანი გაყოფის დახმარებით ვამოწმებთ რიცხვი ლუწია თუ კენტი
#     """
#     if number % 2 == 0:
#         return "even"
#     else:
#         return 'odd'
#
#
# num = int(input('Enter your number: '))
# print(even_number(num))


# def example_void_function():
#     print("yiyliyo")
    # return None
    # return "yiyliyo"

# print(example_void_function())


# def hello_twice():
#     print('Hello', end="           ")
#     print('Hello')
#     print('Hello')
#
# hello_twice()

# def hello_name(my_name):
#     print('Hello', my_name)
#
#
# hello_name()
# hello_name('Ann')

def average_numb(a=10, b=7):
    res = (a+b)/2
    return res


# print(average_numb(a))
# n = int(input("Enter first number: "))
# m = int(input("Enter second number: "))

# x = average_numb(2,6)
# y = average_numb(10,6)
# print(average_numb(n, m))
# print(x, y)


