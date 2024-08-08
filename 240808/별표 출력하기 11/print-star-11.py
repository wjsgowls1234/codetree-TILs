n=int(input())

for i in range(n*2+1):
    for j in range(n*2+1):
        if i==0 or i==n-1 or i==(n-1)*2 or i==(n-1)*3 or j==0 or j==n-1 or j==(n-1)*2 or j==(n-1)*3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()