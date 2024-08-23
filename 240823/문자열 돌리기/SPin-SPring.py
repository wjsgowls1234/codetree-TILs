str= input()
L = len(str)

print(str)
for i in range(L):
    str = str[-1] + str[:-1]
    print(str)