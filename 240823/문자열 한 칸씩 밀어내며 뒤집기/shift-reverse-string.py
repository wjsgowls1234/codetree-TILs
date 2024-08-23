str, q = input().split()
q = int(q)

for i in range(q):
    n = int(input())

    a = str[1:] + str[0]
    b = str[-1] + str[:-1]
    c = str[::-1]

    if n == 1:
        str = a
    elif n == 2:
        str = b
    else:
        str = c

    print(str)