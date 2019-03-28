# -*- coding: utf-8 -*-

a=18
print(bin(18))  #0b 二进制
print(oct(18))  #0o 八进制
print(hex(18))  #0x 十六进制

print(int('0x12',16))
print(int('0o22',8))
print(int('0b10010',2))




#位运算  左移 *2    有意 /2
print(5<<1)  #左移一位 5*2=10
print(3<<1)  #左移一位 3*2=6
print(8>>1)  #右移一位 8/2=4
print(8>>2)  #右移两位 (8/2)/2=2

#按位与 &   同为1 时才为1
print(9&8)
print(9&5)
#按位与 |   同为0 时才为0
print(9|5)
#按位 异或 ^    只要不相同则为1
print(9^5)
#取反 ~
print(~9)
print(~5)