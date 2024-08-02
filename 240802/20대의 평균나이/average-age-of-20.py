sum_val, cnt = 0, 0

while True:
    a = int(input())
    if 20 <= a <=29:
        sum_val += a
        cnt += 1
    else:
        break

print("%.2f" %(sum_val/cnt))