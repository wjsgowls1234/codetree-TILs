string = input()

for i in range(len(string)):
    if i % 2 == 1:
        print(string[-i], end="")