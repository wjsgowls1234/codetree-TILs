m=int(input())
cnt=0

for _ in range(m):
    n=int(input())
    ans=0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        
        ans += 1
    
    print(ans)