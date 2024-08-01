arr = input().split()
a = int(arr[0])
b = int(arr[1])
sum_val, cnt = 0, 0

for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

print(sum_val, "%.1f" %(sum_val / cnt))