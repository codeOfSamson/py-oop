
class Store:
    def __init__(self, items: list[str])-> None :
        self.items = items
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter > len(self.items) -1:
            raise StopIteration
        current = self.counter
        self.counter += 1
        return self.items[current]

my_store = Store(["candy", "cheese", "coffee"])
for i in my_store:
    print(i)

