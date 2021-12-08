class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count +=1
        self.count=100
    def get_selfCount(self):
        return self.count

s=Student("S")
print(Student.count)
print(s.get_selfCount())
