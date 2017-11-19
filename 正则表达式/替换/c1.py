#coding:utf-8

import re

#需求 :从下面的字符串吧c#替换成GO语言
a = 'C|C++|Java|C#|Python|Javascript|PythonC#C#'

def convert(value):
    matched = value.group()
    return '!!' +matched +'!!'

# r = re.sub('C#','Go',a)  #运行:C|C++|Java|Go|Python|Javascript|PythonGoGo  默认是0
# r = re.sub('C#','Go',a ,0)  #运行:C|C++|Java|Go|Python|Javascript|PythonGoGo  0表示这样的替换无限制替换下去
# r = re.sub('C#','Go',a ,1)  #运行:C|C++|Java|Go|Python|Javascript|PythonC#C#  1表示1次
r = re.sub('C#',convert,a ,0)  #运行:C|C++|Java|Go|Python|Javascript|PythonC#C#  1表示1次

#其实这个跟replace函数也是一样的  这就是sub的简化版
#r = r.replace('C#','Go') #运行:C|C++|Java|Go|Python|Javascript|PythonGoGo

#print(r)



#需求:找出这里面所有的数字  凡是大于等于6的就替换成9
s = "A8C342D86"
def replace_dali(value):
    matched = value.group()
    if int(matched) >= 6:
        return "9"
    else:
        return "0"
#\d找到[0-9]   \D(等于[^0-9])
s2 =re.sub('\d',replace_dali,s)

print(s2)  #输出来A9C000D99




#需求:找出这里面所有的数字  凡是大于等于50的就替换成100 小于10的替换成0
s2 = "A812C34132D81236E1"
def replace_da(value):
    matched = value.group()
    if int(matched) >= 6:
        return "9"
    else:
        return "0"
#\d找到[0-9]   \D(等于[^0-9])
s2 =re.sub('\d',replace_da,s2)

print(s2)

























