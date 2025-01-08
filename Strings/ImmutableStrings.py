'''
1. Strings are Immutable: Once we declare the string we can't modify it,
   if we try to modify the string it will create new String.

2. If new string does not have any reference variable then it will be removed.

3. Python Internally uses String Interning.

4. String Interning is the process of Checking sring Intern Pool before creating any new object.

5. Whenever we want to create new object, Python first will check string intern pool,
   weather that object already exists or not.

6. When Object already exist in the string intern Records then address
   of existing object will be reused.
'''

# s1 = 'kodnest'
# s1 = s1.upper()
# print(s1)

# s1 = 'K'
# print(s1, id(s1)) 

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print('s1 Id of H:', id(s1[0])) 
print('s2 Id of w:', id(s2[0]))

print('s1 Id of o:', id(s1[-1])) 
print('s2 Id of o:', id(s2[1]))

print('s1 Id of l:', id(s1[-2])) 
print('s1 Id of l:', id(s1[3])) 
print('s2 Id of l:', id(s2[-2]))