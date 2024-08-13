n=int(input())
arr=list(map(int, input().split()))
reversed_arr=arr[::-1]

for elem in reversed_arr:
    if elem % 2 == 1:
        continue

    print(elem, end=" ")