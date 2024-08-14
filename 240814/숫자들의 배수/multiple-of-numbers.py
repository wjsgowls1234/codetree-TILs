n=int(input())

arr=[1,2,3,4,5,6,7,8,9,10]
new_arr=[]
cnt=0

new_arr=[elem*n for elem in arr]

for elem1 in new_arr:
    if cnt == 2:
        break
    if elem1 % 5 == 0:
        cnt += 1
    print(elem1, end=" ")