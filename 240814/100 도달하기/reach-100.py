n=int(input())

arr=[0,0]
arr[0], arr[1]=1, n

for elem in arr: 
    arr.append(arr[-1] + arr[-2])
    print(elem, end=" ")
    if elem > 100:
        break