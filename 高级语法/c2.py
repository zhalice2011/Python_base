
#coding:utf-8

#一个函数可以被另外一个函数调用并且被当做返回结果
def fuc():
    def fucinner():
        print("我是内部的函数")
    return fucinner

f = fuc()  #此时的f其实就等于里面返回的函数fucinner了
#f() #调用f  #返回的是 "我是内部的函数"


#闭包  : 函数+环境变量
def func():
    a = 25
    def funcinner(x):
        a=100
        return a
    funcinner(1)
    print(a)
    return funcinner

a=100
#f = func()  #此时的f其实就等于里面返回的函数fucinner了
#print(f(2)) #调用f  #返回100的是还是 25*2*2



#课后作业


#每一次都保存上次的记录
# origin = 0
# def go(step):
#     global origin
#     a=origin+step
#     origin=a
#     return origin
# print(go(1))  #第一次走两步
# print(go(2))  
# print(go(3))  


#课后作业


#闭包每一次都保存上次的记录
origin = 0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos +step
        pos = new_pos
        return new_pos
    return go
total = factory(origin)
print(total(2))
print(total(3))
print(total(5))


