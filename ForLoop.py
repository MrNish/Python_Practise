'''
for control_variable in range()
'''

# for i in 'Kodnest':
#     print(i)

# for j in [10, 20, 30]:
#     print(j+10)

# for i in range(1, 6): # range(inclusive, exclusive)
#     print(i)

# for num in range(11, 21, 2):
#     print(num, end = " ")

# for i in range(5):
#     print(i, end = " ")

# # even numbers from 1 to 10
# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num, end = " ")

i = 0
while i < 10:
    print(i + 100)
    i += 1

for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i)

for i in range(1, 11):
    if i == 5:
        break
    else: 
        print(i)