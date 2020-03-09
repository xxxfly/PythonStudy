class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay = int(self.pay*(1+percent))
    
    def __str__(self):
        """打印一个对象会显示对象的__str__方法所返回的内容，要么自己定义一个该方法，要么从一个超类继承一个该方法"""
        return '[Person:%s , %s]'%(self.name,self.pay)


class Manager(Person):
    """子类继承"""
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay)

    def giveRaise(self,percent,bons=.10):
        """定制方法"""
        # self.pay = int(self.pay*(1+percent+bons))
        Person.giveRaise(self,percent+bons)

class Department():
    def __init__(self,*args):
        self.members=list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def shwoAll(self):
        for person in self.members:
            print(person)



# 模块被导入时 会答应模块的名称 person
print(__name__)
# 如果该文件是模块文件，此处可以用来运行测试
if __name__ == '__main__':
    # 测试内容
    bob = Person('Bob Smith')
    sue = Person('Sue Jones',job='Worker',pay=10000)
    print(bob.name,bob.job,bob.pay)
    print(sue.name,sue.job,sue.pay)

    print('*'*30)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(0.2)
    print(sue.pay)

    print('*'*30)
    print(bob)
    print(sue)

    print('*'*30)
    # tom=Manager('Tom Jones','mgr',20000)
    tom = Manager('Tom Jones',20000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)

    print('*'*30)
    development = Department(bob,sue)
    development.addMember(tom)
    development.giveRaises(0.1)
    development.shwoAll()


