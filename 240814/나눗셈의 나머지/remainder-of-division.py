a, b = input().split()
a, b = int(a), int(b)
cnt1, cnt2=0, 0
arr=[]

while a > 1:
    for i in range(b+1):
        if a % b == i:
            arr.append(i)
            cnt2 += 1
    
    a = a // b
    cnt1 += 1
    count_arr=[0]*(cnt1+1)

    for elem in arr:
        count_arr[cnt2] += 1

    sum_val = 0
    for i in range(1,cnt1+1):
        new_count_arr=[elem2**2 for elem2 in count_arr]
        sum_val += new_count_arr[i]

print(sum_val)