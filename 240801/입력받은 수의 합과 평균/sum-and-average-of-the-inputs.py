n = int(input())
sum_val = 0

for _ in range(n):
    a = int(input())
    sum_val += a

print(sum_val, "%.1f" %(sum_val / n))