n=int(input())

for i in range(n):
    for j in range(n):
        x='A'
        print(chr(ord(x)+i), end="")