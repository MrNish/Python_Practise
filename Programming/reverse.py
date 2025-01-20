# reverse() will reverse the original object
li = [10, 20, 30, 40]
print('Before Reverse', li)
li.reverse()
print('After Reverse', li)

# reverse(object): 
li2 = [11, 6, 8, 22]
rev_li2 = list(reversed(li2))
print(li2)
print(rev_li2)

li3 = [1, 5, 2,9]
new_li3 = list(reversed(li3)) # creating new reverse list 
li3.reverse() # Reversing the original list