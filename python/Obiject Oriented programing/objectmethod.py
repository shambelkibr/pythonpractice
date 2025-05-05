class Animal:
    def __init__(self, name, sound):
        self.name = name  # Attribute (Encapsulation)
        self.sound = sound
    
    def speak(self):  # Method (Behavior)
        return f"{self.name} says {self.sound}"

# Creating an object (Instance of a class)
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

# Using the object's method
print(dog.speak())  # Output: Dog says Woof
print(cat.speak())  # Output: Cat says Meow


