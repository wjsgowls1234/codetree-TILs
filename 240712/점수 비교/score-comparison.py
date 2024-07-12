a=input().split()
b=input().split()

a_m=int(a[0])
a_y=int(a[1])

b_m=int(b[0])
b_y=int(b[1])

if a_m > b_m and a_y > b_y:
    print(1)
else:
    print(0)