

#coding:utf-8

#类 = 面对对象
#类 和对象


class Student():
    name = '我是类变量'
    age = 18
    city = '北京'
    sun=10
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        self.__score=0   #初始化分数
        #self.__class__.sun+=1
        print("name",name)
        # print("age",age)
        # print("sum",Student.sun)
        # print("当前学生的总是为sum+self",self.__class__.sun)

    def print_file(self):
        print('name: ' +self.name)
        print('age: ' +str(self.age))
        print('city: ' +self.city)

    @classmethod
    def plus_sum(cls):
        cls.sun+=1000
        print("类别方法里面的",cls.sun)

    @staticmethod
    def add(x,y):
        print("这是我的静态方法",str(Student.sun))

    #给同学打分的方法
    def marking(self,score):
        if score<0:
            return "不能给同学打负分"
        self.__score=score
        print(self.name+str(self.__score))
        return "打分成功"

    #私有的方法

#实例化上面的类
student1 = Student("周达理",29,"厦门1")
print(student1.marking(50))


#print(student1.__score)

student1.__score=1
student1._Student__score=2

print(student1.__score)
print(student1.__dict__)

# student1.plus_sum()
# student1.add(1,2)
# Student.add(1,2)
# student2 = Student("周达理2",29,"厦门2")
# student2.plus_sum()
# student3 = Student("周达理3",29,"厦门3")
# student3.plus_sum()
# print(student.__dict__)
# print(Student.__dict__)


#student.print_file()
#
# 调用类下面的方法
#student.__init__()

class StudentHomework():
    homework_name:'寒假作业'


# 通过marking方法
    