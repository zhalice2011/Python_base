#coding:utf-8
#人的类别

class People():
    sum = 0
    #初始化函数
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #定义一个实例方法
    def get_name(self):
        print("此人名叫"+self.name)
         
    def ceshi(self):
        print("此人名叫"+self.name)
    
    def do(self):
        print("我是父亲类别的do方法")