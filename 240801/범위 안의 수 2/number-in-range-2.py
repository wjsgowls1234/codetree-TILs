sum_val, cnt = 0, 0

for _ in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        sum_val += a
        cnt += 1

print(sum_val, "%.1f" %(sum_val / cnt))