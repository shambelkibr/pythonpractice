class car:
    def __init__(self,model,year,color,for_sale):
        self.model =model
        self.year=year
        self. color=color
        self.for_sale=for_sale
    def drive(self):
        print(f"you drive the car {self.model}  ")
    def stop(self):
        print(f"you stop the car color is {self.color} ")