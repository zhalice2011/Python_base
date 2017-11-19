

#coding:utf-8

#类 = 面对对象
#类 和对象

from people import People

#学生类需要继承
class Student(People):
    def __init__(self,school,name,age):
        self.school =school
        # 在子类里面调用父类的构造函数,
        # People.__init__(self,name,age)
        # supre父类的关键字  参数 1.子类 2.self
        super(Student,self).__init__(name,age)
    def do(self):
        super(Student,self).do()
        print("我是子类别的do方法")


    #私有的方法

#实例化上面的类
student1 = Student("内蒙古科技大学","周达理",29)
print(student1.name)
print(student1.age)
#student1.ceshi()
student1.do()



#然后让学生继承人的类别