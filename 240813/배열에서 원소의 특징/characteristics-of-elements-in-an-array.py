arr=list(map(int, input().split()))
cnt=0

for elemt in arr:
    if elemt % 3 == 0:
        break
    cnt += 1

print(arr[cnt-1])