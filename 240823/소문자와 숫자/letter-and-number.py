str = input()

for elem in str:
    if elem.isalpha() or elem.isdigit():
        print(elem.lower(), end="")