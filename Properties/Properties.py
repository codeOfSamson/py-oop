
class Climber:
    default_grade = "v1"
    def __init__(self, fname, lname, max_grade):
        self.fname = fname
        self.lname = lname
        self._max_grade = max_grade
    
    @property
    def max_grade(self):
        return self._max_grade

    
    @max_grade.setter
    def max_grade(self, new_grade):
        if new_grade.startswith('v') and new_grade[-1].isdigit():
            self._max_grade = new_grade
            return
        raise ValueError("Grade is not correct")

    @max_grade.deleter
    def max_grade(self):
        self._max_grade = Climber.default_grade
        print(f"Grade reset{Climber.default_grade}")
    
sam = Climber("Sam", "Flavin", "v5")
sam._max_grade = "v3"
print(sam.max_one)