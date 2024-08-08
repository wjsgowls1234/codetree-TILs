n=int(input())

for i in range(n):
    for j in range(n):
        a = n - i
        b = n - j
        print("(%d,%d)" %(a,b), end=" ")
    print()