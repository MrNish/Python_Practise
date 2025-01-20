# # If string is holding integer then it can be converted into int.
# a = '30'
# b = int(a)
# print(a, type(a))
# print(b, type(b))

# # str to integer conversion is not allowed
# x = 'Code'
# print(x, type(x))
# # y = int(x)  #Invalid literal for int()
# # print(y, type(y))

# # float
# p = float(input("Enter float type data")) #12.22
# print(p, type(p))

# bool()
'''
1. While converting int to bool for all non zero values we will get True.
2. While converting int to bool for 0 and empty strings we well get False.
'''
q = 0 
print(q, type(q))
q = bool(q)
print(q, type(q))