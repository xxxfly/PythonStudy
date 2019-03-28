# -*- coding: utf-8 -*-
import re

# match() 方法判断是否匹配，如果匹配成功，返回一个 Match 对象，否则返回 None。
# print(re.match(r'00\d','007'))
# print(re.match(r'00\d','07'))
# print(re.match(r'00\w','00A'))

# print(re.match(r'py.','py1'))
# print(re.match(r'py.','pyc'))
# print(re.match(r'py.','py*'))
# print(re.match(r'py.','py.'))

# print('-----<+>----')
# print(re.match(r'\d+',''))
# print(re.match(r'\d+','1'))
# print(re.match(r'\d+','12'))
# print(re.match(r'\d+','1a'))
# print('-----<*>----')
# print(re.match(r'\d*',''))
# print(re.match(r'\d*','ab'))
# print(re.match(r'\d*','1ab'))
# print('-----<{n}>----')
# print(re.match(r'\d{3}','1'))
# print(re.match(r'\d{3}','123'))
# print(re.match(r'\d{3}','1234'))
# print(re.match(r'\d{3}','12a'))
# print('-----<{m,n}}>----')
# print(re.match(r'\d{1,2}',''))
# print(re.match(r'\d{1,2}','1'))
# print(re.match(r'\d{1,2}','12'))
# print(re.match(r'\d{1,2}','123'))
# print(re.match(r'\d{1,2}','1a'))
# print(re.match(r'\d{1,2}','a'))
# print('-----<?>----')
# print(re.match(r'\d?',''))
# print(re.match(r'\d?','1'))
# print(re.match(r'\d?','12'))


# print('-----<[]>----')
# print(re.match(r'[a-z\-]','1'))
# print(re.match(r'[a-z\-]','-'))
# print(re.match(r'[a-z\-]','a'))
# print(re.match(r'[a-z\-]','a-'))
# print(re.match(r'[a-z\-]','-b'))
# print('-------------')
# print(re.match(r'[A-Z][a-z0-9]*','a'))
# print(re.match(r'[A-Z][a-z0-9]*','A'))
# print(re.match(r'[A-Z][a-z0-9]*','Ab'))
# print(re.match(r'[A-Z][a-z0-9]*','A0'))
# print(re.match(r'[A-Z][a-z0-9]*','AB'))

# print('-----<|>----')
# print(re.match(r'(p|P)ython','python'))
# print(re.match(r'(p|P)ython','Python'))
# print(re.match(r'(p|P)ython','Aython'))
# print(re.match(r'(p|P)ython','py'))

# print('-----<^>----')
# print(re.match(r'^[A-Z]{2,3}','A'))
# print(re.match(r'^[A-Z]{2,3}','AB'))
# print(re.match(r'^[A-Z]{2,3}','ABC'))
# print(re.match(r'^[A-Z]{2,3}','Ab'))
# print(re.match(r'^[A-Z]{2,3}','aB'))
# print(re.match(r'^[A-Z]{2,3}','ABCD'))


# print('-----<$>----')
# print(re.match(r'[a-z]{1,2}$','A'))
# print(re.match(r'[a-z]{1,2}$','a'))
# print(re.match(r'[a-z]{1,2}$','aA'))
# print(re.match(r'[a-z]{1,2}$','Ab'))
# print(re.match(r'[a-z]{1,2}$','ab'))
# print(re.match(r'[a-z]{1,2}$','1ab'))
# print(re.match(r'[a-z]{1,2}$','cab'))


#re.match()
# test='要匹配的字符串'
# if re.match(r'正则表达式',test):
#     print('ok')
# else:
#     print('failed')


#切分字符串
# str1='a b  c'
# print(str1.split(' '))
# print(re.split(r'\s+',str1))
# print(re.split(r'[\s\,]+','a,b  c  d'))
# print(re.split(r'[\s\,\;]+','a,b, c;d;;e'))


#分组
# m=re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
# print(m)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# t='05:55:30'

# m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
# print(m.groups())

#贪婪匹配

# print(re.match(r'^(\d+)(0*)$','1023000').groups())
# #非贪婪匹配
# print(re.match(r'^(\d+?)(0*)$','1023000').groups())


#编译
re_telphone=re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
print(re_telphone.match('010-123456').groups())
print(re_telphone.match('010-08820').groups())

