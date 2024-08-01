n = int(input())

for _ in range(n-1):
    n = int(input())

sum_val = 0

for i in range(1,n+1):
    if i % 2 == 1 and i % 3 == 0:
        sum_val += i

print(sum_val)