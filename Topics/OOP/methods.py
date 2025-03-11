# class Rectangle:
#    '''Docstring text here'''
#
#    def __init__(self, width, length=1):
#        self.width = width
#        self.length = length
#
#    def perimeter(self):
#        return 2 * (self.width + self.length)
#
#    def __str__(self):
#        return (f"Hi, I'm rectangle with \nwidth: {self.width}"
#                f"\nlength: {self.length}")
#
#
# rectangle1 = Rectangle(3,5)
# rectangle2 = Rectangle(10,912836)
# print(rectangle1.width)
# print(rectangle1)
# print(rectangle2)
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#
# point1 = Point(3, 4)
# print(point1)
#


# class Student:
#    def __init__(self, firstname, lastname):
#        self.firstname = firstname
#        self.lastname = lastname
#
#    def get_name(self):
#        return self.firstname
#
#    def set_name(self, text):
#        self.firstname = text
#
#
# st1 = Student("Giorgi", "Abashidze")
# print(st1.firstname) # პირდაპირი წვდომა ცვლადზე - არაა რეკომენდირებული
# print(st1.get_name()) # ცვლადზე წვდომა getter მეთოდით
# st1.firstname = "Davit" # ცვლადის მნიშვნელობის შეცვლა მინიჭებით- არაა რეკომენდირებული
# st1.set_name("Davit") # ცვლადის მნიშვნელობის შეცვლა setter მეთოდით
# print(st1.get_name())


# class Student:
#    def __init__(self, firstname, lastname):
#        self.__firstname = firstname
#        self.__lastname = lastname
#        # self._password = password
#
#    def get_firstname(self):
#        return self.__firstname
#
#    def set_firstname(self, text):
#        self.__firstname = text
#
#    def del_name(self):
#        del self.__firstname
#
#    name = property(get_firstname, set_firstname, del_name)
#
#
# st1 = Student('Giorgi', 'Arveladze')
# print(st1.get_firstname())
# st1.name = "Davit"
# print(st1.name)
# del st1.name
# print(st1.name)




# st1 = Student("Giorgi", "Abashidze", "password")
# print(st1.get_firstname())
# st1.set_firstname("Davit")
# print(st1.get_firstname())



class Celsius:

    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, text):
        self.__temperature = text

    def del_temp(self):
        del self.__temperature

    temperature = property(get_temp, set_temp, del_temp)


obj1 = Celsius(16)
obj2 = Celsius(32)
print(obj1.temperature)
obj1.temperature = 18
print(obj1.temperature)