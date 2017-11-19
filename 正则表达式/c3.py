
#coding:utf-8

import re

#需求 :从下面的字符串提取所有的数字
a = 'asdfadf&s*123(1$3___'
#概括字符集
r = re.findall('\d',a)      #等价于[0-9]
r1 = re.findall('\D',a)     #等价于[^0-9]
r2 = re.findall('\w',a)     #等价于[A-Za-z0-9_]   \w只能配所有的单词字符
r3 = re.findall('\W',a) 
print(r)
print(r1)
print(r2)
print(r3)





























