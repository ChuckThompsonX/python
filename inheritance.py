class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "Animal Sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def sound(self):
        return "Meow"

animal = Animal("Animal")
dog = Dog("Sam", "German Shepherd")
cat = Cat("Basil", "Domestic Short Haired")

print(animal.name + ": " + animal.sound())
print(dog.name + ": " + dog.sound())
print(cat.name + ": " + cat.sound())
