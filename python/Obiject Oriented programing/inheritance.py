class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f" the {self.name} speak sound")
        
class cat(animal):
    pass
    def __init__(self, name):
        super().__init__(name)
cat1=cat("whiskers")
cat1.speak()