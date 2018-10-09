class Student:
    def __init__(self, name, school):
        self.name = name,
        self.school = school,
        self.marks = []

    def average(self):
        return sum(self.marks) /len(self.marks)

    @classmethod
    def friend(cls, friend_name):
        return cls(friend_name, self.school)

anna = Student('anna', 'Oxford')

friend = anna.friend('greg')


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent('anna','oxford', 20)

print(anna.salary)
