
#coding:utf-8

#1.匿名函数 lambda
f = lambda x,y:x+y
print(f(1,2))

#等价于下面的普通函数
def add(x,y):
    return x+y

def san(x,y):
    print("x>y") if  x>y  else print("x<y")
    #x>y ? print("达理") : print("不达理")

san(50,7)