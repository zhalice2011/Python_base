#coding:utf-8



import time
#装饰器
def decorator(func):
    def warpper(*args,**kw):   #**kw只是  代表keyword关键字
        print(time.time())
        func(*args,**kw)
    return warpper

@decorator
def f1(a,b,**kw):    #**kw 是关键字参数
    print("我就是"+a)
    print("我就是"+b)
    print(kw)

f1("a","b",c=1,d=2,e="123")

