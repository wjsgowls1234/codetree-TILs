n=int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

print("", end="")

for i in range(n):
    for j in range(i):
        print(" ", end="")

    for j in range(n-i):
        print("*", end="")

    print()