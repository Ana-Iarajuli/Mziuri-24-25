class Shape:
    def __init__(self, color):
        self.color = color

    def say_hi(self):
        print(f'I am a shape with {self.color} color')


class Quadrangle(Shape):
    def __init__(self, a, b, c, d, color):
        super().__init__(color)
        self.a, self.b, self.c, self.d = a, b, c, d
    def say_hi(self):
        print(f'Iam a quadrangle with {self.color} color')


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        # Shape.__init__(self, color)
        self.a = a
        self.b = b
        self.c = c
    def say_hi(self):
        print(f'I am a triangle with {self.color} color')


class Square(Quadrangle):
    def __init__(self, a, color):
        Shape.__init__(self, color)
        self.a = a



# s1 = Shape('red')
# s1.say_hi()
# q1 = Quadrangle(1, 2, 3, 4, 'blue')
# q1.say_hi()
t1 = Triangle(1, 2, 3, "yellow")
t1.say_hi()
#
# print(isinstance(q1, Shape)) # boolean
# print(isinstance(q1, Triangle)) # boolean
#
# print(issubclass(Shape, object))




class Right:
    def __init__(self, name):
        self.name = name
    def call(self):
        print("Right")

class Left:
    def call(self):
        print("Left")


class Bottom(Right, Left):
    pass


obj1 = Right()
obj1.call()

obj = Bottom()
obj.call()


