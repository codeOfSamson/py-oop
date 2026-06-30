
class Employee:
    company = "Apple"
    def __init__(self, name, age):
        self._data = {"name": name, "age": age, "company": Employee.company}
    
    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        return KeyError(f"{key} does not exist!")
    
    def __setitem__(self, key, value):
        if key == "age":
            if not isinstance(value, int):
                raise TypeError("Age must be an int")
        self._data[key] = value

    

john = Employee("Dr.John", 33)
print(john["ages"])
john["age"] = 123
print(vars(john))

        