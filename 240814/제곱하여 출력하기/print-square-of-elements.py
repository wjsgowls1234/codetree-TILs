n=int(input())

arr=list(map(int, input().split()))

new_arr=[elem**2 for elem in arr]

for elem1 in new_arr:
    print(elem1, end=" ")