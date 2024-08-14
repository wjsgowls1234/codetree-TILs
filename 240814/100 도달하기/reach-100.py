n=int(input())

arr=[0,0,0]
arr[1], arr[2]=1, n

for i in range(1, 11): 
    arr.append(arr[-1] + arr[-2])
    print(arr[i], end=" ")
    if arr[i] > 100:
        break