class people:

    def __init__(self, age):
        self.__age = age
    def get_age (self):
        return self.__age

p = people(18)
p.__age=10
p.__people__age=20
print(p.get_age())
print(p.__age)
print(p.__people__age)
f=people.get_age
print(people.get_age)
print(p.get_age)
