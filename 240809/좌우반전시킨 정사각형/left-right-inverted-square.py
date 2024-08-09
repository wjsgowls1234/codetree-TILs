n=int(input())

for i in range(1,n+1):
    for j in range(1,1+n):
        print(i*(n-j+1), end=" ")
    print()