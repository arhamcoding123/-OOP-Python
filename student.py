class StudentProfile:
    def __init__(self,name,id,cgpa):
        self.name=name
        self._id=id
        self.___cgpa=cgpa
    def show_cgpa(self):
        return self.___cgpa

my_student=StudentProfile("Tanvir",101,3.75)


print(f"Student Name:{my_student.name}")
print(f"ID:{my_student._id}")
print(f"CGPA:{my_student.show_cgpa()}")