arr=list(map(int, input().split()))
n=len(arr)
cnt=0
sum_val1=0
sum_val2=0

for i in range(1,n+1,2):
    sum_val1 += arr[i]
print(sum_val1, end=" ")

for i in range(1,n,2):
    sum_val2 += arr[i]
    cnt += 1
avg=sum_val2/cnt
print(f"{avg:.1f}")