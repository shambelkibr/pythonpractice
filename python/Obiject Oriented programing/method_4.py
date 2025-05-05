"""Create a class Car with:

A class attribute wheels set to 4 (shared by all cars).
Instance attributes make and model.
A method describe that prints: "This car is a <make> <model> with <wheels> wheels."
Create two car objects and call the describe method for each."""


# # create class 
# class car:
#     wheels= ["start","stop","classical","light"] # class attributes
    
#     def __init__(self,make,made):
#         self.make=make
#         self.made=made
#     def describe(self):
#         print(f"the car is from  {self.make} and the car is made {self.made} and the car is properties{car.wheels} ")
# car1=car ("steel","transport")
# car1.describe() 

    
class Car:
    wheels = 4  # Class attribute shared by all objects

    def __init__(self, make, model):
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute

    # Method to describe the car
    def describe(self):
        print(f"This car is a {self.make} {self.model} with {Car.wheels} wheels.")

# Creating car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling the describe method
car1.describe()  # Output: This car is a Toyota Corolla with 4 wheels.
car2.describe()  # Output: This car is a Honda Civic with 4 wheels.

    
    
    
    