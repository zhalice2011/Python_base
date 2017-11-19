#coding:utf-8



# CONDITION = True

# i=1
# while i <= 10:
#     i=i+1
#     print(i) 
# else:
#     print("玩了这么多把终于打到了最强王者") 

#while的使用场景   上王者使用while  设定一个目标 达到目标就不执行了

#递归算法里面用while是非常合适的

#for的使用场景  遍历序列或者集合 或者字典

a = ['apple','orange','banna','grage']
c = [['apple','orange','banna','grage'],(1,2,4)]
b = {'达理',"2",34}

for x in c:
    for y in x:
        print(y,end='\n')
else:
    print("当遍历结束的时候就会被执行")


a= [1,2,3,4]

for x in a:
    print(x)
    if x==3:
        break
    print("循环结束啦")

for x in a:
    print(x)
    if x==3:
        continue
    print("循环结束啦")