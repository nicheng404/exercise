class Animal:
    a=2
    def __init__(self):
        self.a=1
    pass

class Dog(Animal):
    a=4
    # def __init__(self):
    #     self.a=5
    pass


print(Dog().a)