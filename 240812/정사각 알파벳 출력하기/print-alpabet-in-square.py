n=int(input())
cnt=0

for i in range(n):
    for j in range(n):
        x='A'
        print(chr(ord(x)+cnt), end="")
        cnt += 1
    print()