for _ in range(10):
    n = int(input())

cnt = 0
for n in range(1,11):
    if n % 2 == 1:
        cnt += 1
print(cnt)