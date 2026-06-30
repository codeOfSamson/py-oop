
class Ship:
    def __init__(self, crew:int, length:int):
        self.crew = crew
        self.length = length

    def __str__(self):
       return  f"Crew:{self.crew}, Length:{self.length}"
    
    # def __repr__(self):
    #    return  f"Ships({self.crew}, {self.length})"

ship = Ship(5, 55)
ship_b = Ship(6,66)
print(ship)
ships = [ship, ship_b]
print(ships)

    