class Person:
      def __init__(self, firstname='shambel ', lastname='kibre', age=21, country='ethiopia', city='debre brhain'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'abebe', 30, 'ethopia', 'debre brhan')
print(p2.person_info())