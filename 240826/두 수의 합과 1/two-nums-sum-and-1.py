a, b = tuple(map(int, input().split()))
cnt = 0

sum_val = a + b
sum_val = str(sum_val)

for elem in sum_val:
    if elem == '1':
        cnt += 1

print(cnt)