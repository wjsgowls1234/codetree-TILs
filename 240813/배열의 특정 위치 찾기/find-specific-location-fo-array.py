arr=list(map(int, input().split()))
cnt=0
sum_val1=0
sum_val2=0

for i in range(10):
    if (i+1) % 2 == 0:
        sum_val1 += arr[i]

    #if (i+1) % 3 == 0:
     #   sum_val2 += arr[i]
      #  cnt += 1
print(sum_val1, end=" ")

for i in range(10):
    if (i+1) % 3 == 0:
        sum_val2 += arr[i]
        cnt += 1
avg=sum_val2/cnt
print(f"{avg:.1f}")