#! /usr/bin/env python3

f = open('./workfile', 'rb')
print(f.read())

f = open('./workfile', 'rb')
print(f.readline())

f = open('./workfile', 'rb')
print(f.readlines())

f = open('./workfile', 'rb') 
for line in f:
    print(line, end='')

f = open('./workfile', 'r+') 
value = ('the answer',42)
f.write(str(value))
f = open('./workfile2', 'r+b') 
f.write(b'01234abcde')

f.seek(5) # Go to the 6th byte in the file
print(f.read(1))
f.seek(-3, 2) # Go to the 3rd byte before the end
print(f.read(1))

f.close()
