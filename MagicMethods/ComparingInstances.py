
class House:
    def __init__(self, bedrooms:int):
        self.bedrooms = bedrooms
    
    def __eq__(self,other)->bool:
        try:
            return self.bedrooms == other.bedrooms
        except AttributeError:
            raise ValueError("Only housees can be compared")   
         
    def __lt__(self,other)->bool:
        return self.bedrooms < other.bedrooms
    
    def __gt__(self,other)->bool:
        return self.bedrooms > other.bedrooms
    
    def __repr__(self)->bool:
        return str(self.bedrooms)
    
    

house_a = House(3)
house_b = House(4)
houses = [house_a, house_b, House(5)]
houses.sort()
print(houses)
print(house_a == house_b)