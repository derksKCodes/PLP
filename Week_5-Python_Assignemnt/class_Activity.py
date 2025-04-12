# Activity 2: Polymorphism challenge
class Vehicles:    
    def __init__(self, brand, model, year, move):
        self.brand = brand
        self.model = model
        self.year = year
        self.move = move       
  
    
class Car(Vehicles):

    def moving(self):
        
        print(f"{self.brand} {self.model} is {self.move}.")
        
class Boat(Vehicles):
    def moving(self):
        
        print(f"{self.brand} {self.model} is {self.move}.")
        
class Plane(Vehicles):
    def moving(self):
        
        print(f"{self.brand} {self.model} is {self.move}.")
        
# Create instances of each class

car = Car("Toyota", "Corolla", 2020, "driving")
boat = Boat("Yamaha", "242X", 2018, "sailing")
plane = Plane("Boeing", "747", 2015, "flying")

for x in [ car, boat, plane]:
    x.moving()
   
    
    