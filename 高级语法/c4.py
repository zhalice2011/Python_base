
#coding:utf-8

#map 类  基本用法 对集合/序列的每一项都会执行这个函数

#需求  求下面的列表的每一个数字的平方 在组成一个新的列表  然后把新的列表打印
list_x = [1,2,4,5,6]
list_y = [1,2,4,5,6]
print(list(map(lambda x,y:x*2+y,list_x,list_y))) #结果[3, 6, 12, 15, 18]
