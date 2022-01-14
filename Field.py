class Counter:
    __secretCount = 4  # 私有变量
    publicCount = 0    # 公开变量

    def __init__(self):
        self.__secretCount =1
        self.publicCount =3
        print(2)

    def get_SelfSecretCount(self):
        return self.__secretCount


class Son(Counter):
    def get_SelfSecretCount(self):
        self.__secretCount = 6
        return self.__secretCount
    pass

s=Son()
print(s.publicCount) # 继承到了实例变量
print(Son.publicCount) # 继承到了类变量
print(s.get_SelfSecretCount()) #


class Daughter(Counter):
    def __init__(self):
        super().__init__()

d=Daughter()

print(list([1,2,3]))
