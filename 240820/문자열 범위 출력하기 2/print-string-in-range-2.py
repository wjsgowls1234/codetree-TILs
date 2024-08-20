string = input()
n = int(input())

for i in range(n):
    if n > len(string):
        print(string[-1], end="")
    else:
        print(string[-i-1], end="")