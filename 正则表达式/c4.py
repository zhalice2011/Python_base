
#coding:utf-8

import re

#需求 :提取java python php这三个语言
#数量词
# 
# 
# r = re.findall('[a-z][a-z][a-z][a-z]',a)      #['pyth', 'java']

# r = re.findall('[a-z]{3}',a)   #['pyt', 'hon', 'jav', 'php']
a = 'pytho1python2pythonn3'
r1 = re.findall('python*',a)  #意思是n这个字符出现0次或者无限多次 #打印出来  ['pytho', 'python', 'pythonn']
r1 = re.findall('python?',a)  #打印出来  ['pytho', 'python', 'python']
r1 = re.findall('python{1,2}?',a)  #打印出来  ['python', 'python']
#r1 = re.findall('python{1,2}',a)  #打印出来  ['python', 'pythonn']


# r1 = re.findall('[a-z]{3,6}',a)   #打印出来['python', 'java', 'php']
# r2 = re.findall('[a-z]{3,6}?',a)   #加文号变成非贪婪模式打印出来['pyt', 'hon', 'jav', 'php']

#print(r1)
#print(r2)




#边界匹配

#验证qq号是不是正确的qq号码   4-8位之间
qq='10000112123'

r = re.findall('\d{4,8}',qq)  #['10000112']  其实不符合但是还是匹配出来了
r = re.findall('^\d{4,8}$',qq)  #[]   前面加上^  后面加上$ 完全匹配

#print(r)




#判断字符串里面是不是有3个python
a = 'pythonpythonpythonpythonpython'

r = re.findall('(python){3}',a)  #['python']


#print(r)


b='PythonC++C#\nJavascript'

r = re.findall('C#',b)  #['C#']  大写
r = re.findall('c#',b)  #[]      小写

r = re.findall('c#',b,re.I)  #['C#']   re.I会忽略大小写
r = re.findall('c#.{1}',b,re.I)  #[]   re.I会忽略大小写  但是.这个符号不能匹配\n
r = re.findall('c#.{1}',b,re.I | re.S)  #结果又能进行匹配了  ['C#\n']




print(r)





