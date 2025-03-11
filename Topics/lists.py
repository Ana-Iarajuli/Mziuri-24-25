# shopping_list = ["axali kartofili", "witeli tyemali", "zeti", "marili"]
# bucket_list = ["kartofilisshewva", "kcxoetshigulao"]
# # shopping_list[3] = "kama"
# # shopping_list[1:4] = ["მწვანე ტყემალი", "კარაქი", "პილპილი"]
# # print(shopping_list[:2])
# # print(shopping_list[2:])
# shopping_list.append("pilpili")
# print(shopping_list)
# print(len(shopping_list))

# is_oil = "Zeti" in shopping_list
# print(is_oil)

# marks = [100, 900, 87, 60, 15]
#
# print(sum(marks)/len(marks))


# for i in shopping_list:
#     print(i, end=",")







# n = 3
# n = 5
# print(n)
# print(f"shen iyide {shopping_list[4]}")
# print(f"sayideli dagrcha {shopping_list[:4]}")

# n = 4
# last_index = 3

# n - 1


# numbers = [1, 2, 10, 6] # რიცხვების ჯამი / რიცხვების რაოდენობაზე
# print(sum(numbers) / len(numbers))
# print(numbers[5][-1])
# name = "jasurbeki"
# print(name[-1])
# numbers.sort()
# print(numbers)



# burgir = ["bun", "sauce", "salatis furceli", "xorci", "yveli", "bun"]
#
# burgir.insert(2, "xaxvi")
# burgir.append("xaxvi")
# burgir.remove("salatis furceli")
# burgir.pop(3)
# burgir.sort()
# del burgir[2]
# burgir.clear()
# print(burgir.count("xaxvi"))
# burgir.reverse()
# print(burgir.index("xaxvi"))
# print(burgir)




# burgir.insert(3, "mjave kitri")
# print(burgir.index("bun2"))
# burgir.pop(5)
# burgir.remove("salatis furceli")
# burgir.clear()
# print(burgir.count("bun"))
# print(burgir)
# print(burgir[10])
# count = 0
# for bun in burgir: # ["bun", "sauce", "salatis furceli", "xorci", "yveli", "bun"]
#     if bun == "mjave kitri":
#         count += 1
# print(count)

# burgir.sort()
# burgir.reverse()
# del burgir[3:5]
# print(burgir)








# სიის შექმნა
# str1 = "chai da karaqiani puri + muraba"
# nums = list(str1)
# print(len(str1)) # ['chai', 'da', 'karaqiani'] 3 || ['c', 'h'...] 2


# range and list
# nums = list(range(0, 20, 2))
# print(nums)


# lists and strings
# str1 = "chai da karaqiani puri-+-muraba"
# print(str1)
# new_str1 = str1.split("-")
# print(new_str1) # ['chai', 'da', 'karaqiani'...]


# burgir = ["bun", "sauce", "salatis furceli", "xorci", "yveli", "bun"]
# new_burgir = " ".join(burgir)
# print(type(new_burgir))


# TUPLE
# nums = (1, 10, 3, 4)
# tuple1 = min(nums)
# print(tuple1)
# print(type(nums))


nums = [1, 2, 3, 4]
# nums.insert(1, "5")
# print(nums)
nums[9] = 5
print(nums)