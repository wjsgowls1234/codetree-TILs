A = input().split()
B = input().split()

Aa = A[0]
As = A[1]

Ba = B[0]
Bs = B[1]

if (int(Aa) >= 19 and As == "M") or (int(Ba) >= 19 and Bs =="M"):
    print(1)
else:
    print(0)