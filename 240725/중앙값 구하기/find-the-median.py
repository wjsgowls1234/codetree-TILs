arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a > b > c:
    print(b)
elif a > c > b:
    print(c)
elif b > a > c:
    print(a)
elif b > c > a:
    print(c)
elif c > a > b:
    print(a)
elif c > b > a:
    print(b)