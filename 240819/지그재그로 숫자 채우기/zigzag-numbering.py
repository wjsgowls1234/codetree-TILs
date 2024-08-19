n, m = tuple(map(int, input().split()))
num = 0

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr_2d[j][i] = num
            num += 1
    else:
        for j in range(n - 1, -1, -1):
            arr_2d[j][i] = num
            num += 1

# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()