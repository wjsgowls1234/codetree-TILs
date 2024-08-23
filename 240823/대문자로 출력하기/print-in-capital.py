str = input()

for elem in str:
    if elem.isalpha():
        print(elem.upper(), end="")