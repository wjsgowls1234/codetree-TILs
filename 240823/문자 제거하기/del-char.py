string = input()
leng = len(string)
arr = list(string)

while leng > 1:
    n = int(input())
    
    if n >= leng:
        n = leng - 1

    arr.pop(n)
    leng -= 1

    string = ''.join(arr)

    print(string)