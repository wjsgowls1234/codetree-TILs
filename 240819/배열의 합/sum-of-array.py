arr_2d = []
sum_val = 0
for _ in range(4):
    arr_1d = list(map(int, input().split()))
    sum_val = sum(arr_1d)
    print(sum_val)