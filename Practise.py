print(bool('Kodnest')) #True
# print(int('kod')) #Error
print(int('11')) # 11  IMP
# print(float('Kodnest')) # Error
print(float('22.22')) # 22.22  IMP
print(bool('')) # False
print(bool(0)) # False
print(bool(12)) #True
# print(int('12.22')) # Error
print(int(12.56)) # 12 we can convert float to int
print(float(12)) # 12.0

#Taking float value from user and converting int into int
value = int(float(input('Enter float value'))) #12.55
print(value, type(value)) # 12 int