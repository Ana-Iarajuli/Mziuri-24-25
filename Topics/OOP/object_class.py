class Rectangle:
    '''ეს კლასი არის მართკუთხედებისთვის'''

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        perimeter = self.width * 2 + self.length * 2
        return perimeter

    # def __str__(self):
    #     return f"ragaxca"


rectangle1 = Rectangle(10, 2, "red")
print(rectangle1)
# rectangle2 = Rectangle(12, 12, "blue")
# per_rec2 = rectangle2.perimeter()
# per_rec1 = rectangle1.perimeter()
# print(per_rec2, per_rec1)
# print(type(rectangle1))
# print(rectangle1.width)
# print(rectangle1.length)




