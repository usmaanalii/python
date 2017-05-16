# Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?


class People:

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


class Teacher(People):

    def __init__(self, name, age, role, room):
        People.__init__(self, name, age, role)
        self.room = room

    def getEmail(self):
        return self.name + '@keele.ac.uk'


class Student(People):

    def __init__(self, name, age, role):
        People.__init__(self, name, age, role)

    def getEmail(self):
        return self.name + '@studentskeele.ac.uk'

ed = Teacher('Ed', 32, 'Director', '21b')
usy = Student('Usmaan', 21, 'ACS student')
print(ed.room)
print(usy.role)
print(ed.getEmail())
print(usy.getEmail())
