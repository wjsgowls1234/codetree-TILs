arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a == min(arr[0:2]):
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b == c:
    print(1)
else:
    print(0)