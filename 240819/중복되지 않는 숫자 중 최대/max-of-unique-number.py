n = int(input())
arr = list(map(int, input().split()))
new_arr = []
default = False

for i in range(n):
    if arr.count(arr[i]) == 1:
        new_arr.append(arr[i])

max_val = 0

if new_arr == []:
    print(-1)
else:
    for elem in new_arr:
        if elem > max_val:
            max_val = elem
    print(max_val)