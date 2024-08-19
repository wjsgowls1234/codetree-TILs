n = int(input())
arr = list(map(int, input().split()))

min_dif = 1
for i in range(n):
    for j in range(1, i):
        dif = arr[i] - arr[j]

        if min_dif > dif:
            min_dif = dif

    for j in range(i + 1, n):
        dif = arr[j] - arr[i]

        if min_dif > dif:
            min_dif = dif
print(min_dif)