#! /usr/bin/env python3
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
# use list as a stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.pop()
print(stack)

#use list as a queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   #Terry arrives
queue.append("Jane")    #Jane arrives
print(queue.popleft())         #The first to arives now leaves
print(queue.popleft())         #The second to arives now leaves
print(queue)

#列表推导式
squares = []
for x in range(10):
    squares.append(x**2)

print("squares of 0 to 10:", squares)

squares2 = [x**2 for x in range(10)]
print("squares2 of 0 to 10:", squares2)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("strip space:",[weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print("展开多维列表:", [num for elem in vec for num in elem])

#nest 
#transport a 3X4 matrix
matrix = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
print("Transport a 3X4 matrix:", matrix, "to 4X3", 
        [[row[i] for row in matrix] for i in range(4)])


print("Transport a 3X4 matrix: use list(zip(*))", matrix, "to 4X3", list(zip(*matrix)))


