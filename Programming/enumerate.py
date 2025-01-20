# lis = [10, 20, 30]
# for idx, ele in enumerate(lis):
#     print(idx, ele)

# WAP to print all even index element
li = [10, 20, 30]
for idx, ele in enumerate(li, start=1):
    if idx % 2 == 0:
        print(f"Index of {ele} is {idx}")