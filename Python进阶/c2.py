#coding:utf-8

#列表推导式
a = [1,2,3,4,5,6]
b = {1,2,3,5,6,6}
#求平方   i**2 也是代表i的平方   i**3表示i的立方  以此类推
b = [i*i for i in a]
b = [i**2 for i in a]              #[1, 4, 9, 16, 25, 36]
b = [i**2 for i in a if i>=5]      #条件筛选  [25, 36]
c = {i**2 for i in b if i>=5}      #条件筛选  {1296, 625}
print(c)