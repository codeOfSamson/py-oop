

class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self._age = age #private

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError("Age needs to be int")
        
    @age.deleter
    def age(self):
        self._age = None


    @property
    def email(self):
        return f"{self.fname}.{self.lname}@mail.com"
    
john = Employee("john", "boy", 40)
print(john.email)
john.lname = "guy"
print(john.email)

print(john.age)
del john.age
print(john.age)
