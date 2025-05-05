# Defining a class
class Animal:
    # Shared structure (attributes)
    species = "Animal"  # Class attribute shared by all objects

    # Constructor to define instance attributes
    def __init__(self, name, sound):
        self.name = name  # Instance attribute (specific to each object)
        self.sound = sound

    # Shared behavior (method)
    def speak(self):  
        return f"{self.name} says {self.sound}"

# Creating objects (instances) of the class
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

# Accessing shared and specific attributes
print(dog.species)  # Output: Animal (shared attribute)
print(cat.species)  # Output: Animal (shared attribute)

# Accessing instance attributes
print(dog.name)  # Output: Dog
print(cat.name)  # Output: Cat
print(dog.sound)
print(cat.sound)
# Using shared behavior (method)
print(dog.speak())  # Output: Dog says Woof
print(cat.speak())  # Output: Cat says Meow
