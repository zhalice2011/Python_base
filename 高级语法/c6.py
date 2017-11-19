
#coding:utf-8
#fillter 过滤
import time

#定义一个打印时间的函数
def print_current_time(func):  #传入一个函数
    print(time.time()) #打印当前的时间  1511087350.033896
    func() #调用传入的函数


def f1():
    print("迟雪妮我喜欢你")


def f2():
    print("迟雪妮我好像不喜欢你了")

print_current_time(f1)
print_current_time(f2)