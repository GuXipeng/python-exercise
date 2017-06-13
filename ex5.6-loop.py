#!/usr/bin/env python3
#for dict use iteritems() func
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#loop tow or more list use zip() func.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

#str.formate()
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#for list can use enumerate() func to return index and value
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# for reversed range loop use reversed()
for i in reversed(range(1, 10, 2)):
    print(i)
#sorted() generates a new sorted list
