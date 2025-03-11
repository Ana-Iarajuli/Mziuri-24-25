# FileNotFoundError
# file = open("jasurbeki.txt")
# content = file.read()

# IndexError
# nums = [1, 2, 3, 4]
# print(nums[5])

# SyntaxError
# print(

# KeyError
# info = {"name": "surname"}
# print(info["fsdjgb"])

# TypeError
# result = "5" + 5
# print(result)

# ----------------------------------------------------
# try-except-else-finally
# if-elif-else
# new_file = open("jasurbeki.txt", "w")

# FileNotFoundError
try:
    # info = {"name": "surname"}
    # print(info["fsdjgb"])
    file = open("jasurbeki.txt")
    # content = file.read()
except FileNotFoundError:
    print("Error")
except KeyError as error_message:
    print(f"this key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("Finished")



try:
    a = input("Input the first number")
    b = input("Input the second number")
    k = int(a) / int(b)
except ZeroDivisionError:
    print("Number is divided by zero")
except ValueError:
    print("There is Value error")
except: # ყველა სხვა შეცდომისთვის
    print("Any other Errors")


def avg(nums):
    assert len(nums) != 0, "list is empty"
    return nums

numbers = []
print(avg(numbers))