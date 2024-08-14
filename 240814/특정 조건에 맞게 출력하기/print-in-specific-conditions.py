arr=list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 1:
        elem += 3
        print(elem, end=" ")
    else:
        elem //= 2
        print(elem, end=" ")