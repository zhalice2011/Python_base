
#coding:utf-8
from functools import reduce
list_x = [1,2,3,4,5,6]
r=reduce(lambda x,y:x+y,list_x)
print(r)  #结果21
#第一次调用取前面两个元素 1+2
#第二次调用取第三个元素 +前面一次的结果 
