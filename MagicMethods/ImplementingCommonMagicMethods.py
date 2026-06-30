
class Plane:
    def __init__(self, seats, length):
        self.seats = seats
        self.length = length
    
    def __len__(self):
        return self.length
    
plane = Plane(123, 40)
print(len(plane))

class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __add__(self, other):
        combined_h = self.height + other.height
        combined_w = self.width + other.width
        return Shape(combined_h, combined_w)
        
a = Shape(10,10)
b = Shape(20,20)
c = a + b
print(vars(c))