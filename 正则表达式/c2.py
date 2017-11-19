#coding:utf-8

import re

#需求 :从下面的字符串提取所有的数字
a = 'C1C++2Java5C#7Python0Javascript1000Python'


b = 'acc, afc, adc, ascsccdc, afsdfc, gdf'

r = re.findall('\d',a)  #打印出来['1', '2', '5', '7', '0', '1', '0', '0', '0']

r = re.findall('\D',a)  #打印出来['C', 'C', '+', '+', 'J', 'a', 'v', 'a', 'C', '#', 'P', 'y', 't', 'h', 'o', 'n', 'J', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't', 'P', 'y', 't', 'h', 'o', 'n']

r = re.findall('a[^a-z]c',b)  #打印出来 ['acc', 'afc'] 

print(r)

#字符集 