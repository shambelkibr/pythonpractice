class person :
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def __str__(self):
          return f"my name is {self.name} and I am {self.age} years old"
p1=person("shambel kibre",23)
print(p1)