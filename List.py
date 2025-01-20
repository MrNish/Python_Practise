'''
1. In list we can stroe Homogenous as well as Hetrogeneous Data.
2. In list we can store Duplicate Values.
3. List is an Ordered Collection of Data: Order of insertion will remain as it is in Output
4. Lists are Mutable: Once we declare the list we can modify it.
'''

li1 = [10, 20, 44, 45, True, 'Kodnest']
print(li1, type(li1))
li1.append(300)
print(li1)

# insert(index, element)
li1.insert(1, 15)
print(li1)

# remove(element): Removes the first occurance of the specified element.
li1.remove(20)
print(li1)

# in and not in Operator:
print(2000 in li1) #false
print('Kodnest' in li1) #True


# pop()
rem = li1.pop()
print(rem)
print(li1)

# pop(index):
rem = li1.pop(4)
print(rem)
print(li1)

# del keyword: Do not return deleted item and it's function
del li1[1]
print(li1)