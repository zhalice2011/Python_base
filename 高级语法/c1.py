#coding:utf-8

#枚举
from enum import Enum

class VIP(Enum):
    yellow = 1
    green = 2
    black = 3
    red = 4

print(VIP(1))  #枚举类型的转换  VIP.yellow

# for v in VIP.__members__:
#     print(v)




















