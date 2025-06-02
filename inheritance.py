class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

dog = Dog("Scooby")
cat = Cat("Whiskers")

print(f"{dog.name} is a dog.")
print(f"{cat.name} is a cat.")
dog.eat()
cat.sleep()