rows = 4
col = 5
# # Box
# for i in range(rows):
#     for j in range(col):
#         print('*',end=' ')
#     print()

# # Increasing Pyramid
# for i in range(rows):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# # Decreasing Pyramid
# for i in range(rows):
#     for j in range(i, rows):
#         print('*',end=' ')
#     print()

# # right-Pascal Trianlge
# for i in range(rows):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(rows):
#     for j in range(i, rows-1):
#         print('*',end=' ')
#     print()

# # Butterfly
# for i in range(rows):
#     for j in range(i+1):
#         print('*',end='')
#     for j in range(i, rows - 1):
#         print(' ', end='')
#     for j in range(i, rows - 1):
#         print(' ', end='')
#     for j in range(i+1):
#         print('*',end='')
#     print()
# for i in range(rows):
#     for j in range(i, rows-1):
#         print('*',end='')
#     for j in range(i+1):
#         print(' ', end='')
#     for j in range(i+1):
#         print(' ', end='')
#     for j in range(i, rows-1):
#         print('*',end='')
#     print()

# Diamond 
for i in range(rows):
    for j in range(i, rows):
        print(" ", end = '')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i, rows-1):
        print('*',end='')
    for j in range(i, rows):
        print('*',end='')
    print()
    