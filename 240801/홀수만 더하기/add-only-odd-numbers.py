n = int(input())
for _ in range(n):
    n = int(input())

sum_val = 0

for i in range(1,n+1):
    if n % 2 == 1 and n % 3 == 0:
        sum_val += i

print(sum_val)