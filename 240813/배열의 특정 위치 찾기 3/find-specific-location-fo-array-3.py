arr=list(map(int, input().split()))
cnt=0

for elem in arr:
    cnt += 1
    if elem == 0:
        break

print(arr[cnt-4] + arr[cnt-3] + arr[cnt-2])