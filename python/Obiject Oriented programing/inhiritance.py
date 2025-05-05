class person:
    def __init__(self,name="sarez",age=12):
        self.name=name
        self.age=age
    def __str__(self):
     return f"my name is {self.name} and I am {self.age} years old"
 
class student(person):
          pass  
x=student("shambel",34)
print(x)