n=int(input())

for i in range(n*2):
    if i % 2 == 1:
        for j in range(n-(i-1)//2):
            print("*", end=" ")
        print()
    else:
        for j in range(i//2+1):
            print("*", end=" ")
        print()