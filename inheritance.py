class people:
    @staticmethod
    def m1():
        print("父类静态方法")

    @classmethod
    def m2(cls):
        print("父类类方法")

class p1(people):
    pass

p1.m2()
p1.m1()

