str = input()

for elem in str:
    if elem.isupper():
        elem = elem.lower()
    else:
        elem = elem.upper()

    print(elem, end="")