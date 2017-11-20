
#coding:utf-8
#需求 字典代替switch
day = 10
def a():
    return a
def b():
    return b

switch = {
    0:a,
    1:b,
}
#day_name = switch[day]
#当 day不等于0-5的时候  就会等于Unkown的这个默认值了
day_name = switch.get(day,'Unkown')()

print(day_name)