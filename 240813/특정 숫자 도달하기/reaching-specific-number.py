arr = list(map(int, input().split()))
cnt=0
sum_val=0

for i in range(10):
    if arr[i] >= 250:
        break
    
    sum_val += arr[i]
    cnt += 1

print(sum_val, end=" ")
avr=sum_val / cnt
print("%.1f" %avr)