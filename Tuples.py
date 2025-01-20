'''
1. In tuples we can store homogeneous and hetroheneous Data.
2. In tuples we can store duplicates
3. Tuples are Immutable Once we declare we can't modify it
'''
tup1 = (10, 20, 55, 'Kodnest', True, 10)
print(tup1)
# tup1.remove(55)
# tup1.pop()
# dep tup1[2]

# del Deletes the complete tup1 object
del tup1
# print(tup1) # Error

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)