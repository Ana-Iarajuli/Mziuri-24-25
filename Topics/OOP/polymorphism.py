class Cat:
    def eat(self):
        print("cat eats")

    def talk(self):
        print("cat talks")

    def walk(self):
        print("cat walks")


class Dog:
    def eat(self):
        print("dog eats")

    def talk(self):
        print("dog talks")

    def walk(self):
        print("dog walks")


c = Cat()
d = Dog()



for action in (c, d):
    print(action.eat())
    print(action.talk())
    print(action.walk())


class Cat:
    def eat(self):
        print("Cat eats milk")

    def talk(self):
        print("Cat says miaww")

    def walk(self):
        print("Cat can run at 20km/h")

class Dog:
    def eat(self):
        print("Dog eats a bone")

    def talk(self):
        print("Dog says aww")

    def walk(self):
        print("Dog can run at 40km/h")

cat = Cat()
dog = Dog()

animals = (cat, dog)

for animal in animals:
    animal.eat()
    animal.talk()
    animal.walk()