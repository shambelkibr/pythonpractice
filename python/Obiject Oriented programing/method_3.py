"""Write a class Person with:

An __init__ method to initialize name and age attributes.
A method introduce that prints: "Hi, my name is <name> and I am <age> years old."
Create an object of the Person class and call the introduce method."""

class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method to introduce the person
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 25)
print(person1.name)
print(person1.age)
person1.introduce()  # Output: Hi, my name is Alice and I am 25 years old.
