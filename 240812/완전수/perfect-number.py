arr=input().split()

start=int(arr[0])
end=int(arr[1])
cnt=0

for i in range(start,end+1):
    sum_val=0
    for j in range(1,i):
        if i % j == 0:
            sum_val += j
    
    if sum_val == i:
        cnt += 1

print(cnt)