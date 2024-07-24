arr1=input().split()
arr2=input().split()

a=int(arr1[0])
b=int(arr1[1])
c=int(arr2[0])
d=int(arr2[1])

if a > c:
    print("A")
elif a < c:
    print("B")
elif a == c and b > d:
    print("A")
elif a == c and b < d:
    print("B")