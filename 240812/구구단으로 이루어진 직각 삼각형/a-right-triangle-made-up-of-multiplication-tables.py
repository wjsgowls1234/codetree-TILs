n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j < n - i + 1:
            print(f"{i} * {j} = {i*j}", end=" / ")
        elif j == n - i + 1:
            print(f"{i} * {j} = {i*j}", end="\n")