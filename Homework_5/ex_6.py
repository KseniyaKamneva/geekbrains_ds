"""
Created on Mon May 23 02:41:09 2022

@author: Ксения Камнева
"""

mydict = {}
with open('6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        elems = [ i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        print(elems)
        name_sum = sum(map(int, "".join(elems).split()))
        mydict[name] = name_sum
print(f"{mydict}")
