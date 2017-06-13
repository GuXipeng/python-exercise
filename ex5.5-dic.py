#!/usr/bin/env python3
#理解字典的最佳方式是把它看做无序的键： 值对 （key:value pairs）集合
tel = {'jack': 4098, 'sape': 4139}
tel['guide'] = 4142
print(tel)
print(tel['jack'])
del tel['sape']
print("list(tel.keys())", list(tel.keys()))
print("sorted(tel.keys())", sorted(tel.keys()))

#dict() function create dic from key-value
tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("tel2:",tel2)
