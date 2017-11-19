#coding:utf-8



#python里面如何使用 for (i=0; i<10; i++)

#想让一段代码执行10次  递增

for x in range(0,10,2):
    print(x,end=" | ")


#递减的等差数列
for x in range(10,0,-2):
    print(x,end=" | ")

#for循环的练习题

b=[1,2,3,4,5,6,7]

for a in range(0,len(b),2):
    print(b[a],end="|")
    
