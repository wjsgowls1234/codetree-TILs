string = input()
n = int(input())

for i in range(n):
    print(string[-i-1], end="")
    if i == n:
        break