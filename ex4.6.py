#! /usr/bin/env python3
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any" ,kind,"?")
    print("-- I'm sorry, we are all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 48)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
    
cheeseshop("Limburger", "It is very funny, sir!",
    "It's really very funny, sir!",
    shopkeeper = "Michael", 
    client = "John",
    sketch = "Chinese shop sketch")
print(f(1))
print(f(2))
print(f(3))
