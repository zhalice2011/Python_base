#coding:utf-8

import re

#需求 :从下面的字符串判断有没有Python
a = 'C|C++|Java|C#|Python|Javascript|Python'

# print(a.index('Python'))  #python内置表达式  打印出来的是14  就是0开始数数  P字母的位置

# print('Python' in a)  #Python内置表达式  存在就是true


r = re.findall('Python2',a)   #从a里面找到所有的Python

print(r)

if len(r) != 0:
    print("字符串里面包含Python")
else:
    print("字符串里面没有Python")   