A = input()
re = input()

for i in range(len(re)):
    if re[i] == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
    
print(A)