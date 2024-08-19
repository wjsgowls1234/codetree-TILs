n = int(input())
arr = list(map(int, input().split()))
new_arr = []
default = False

for i in range(n):
    if arr.count(arr[i]) == 1:
        new_arr.append(arr[i])

max_val = 0
for elem in new_arr:
    if elem > max_val:
        max_val = elem
    elif new_arr == []:
        max_val = -1
print(max_val)