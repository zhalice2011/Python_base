

a=[1,2,3,4,5,6,7,8]




for i in range(0,len(a),2):
    print(i)
    print(a[i],end=" | ")


#python是一门高级语言  提供了很多可以避免我们写for循环
b = a[0:len(a):2]
print(b)
