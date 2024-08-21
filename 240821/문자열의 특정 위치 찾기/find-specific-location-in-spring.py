string = input().split()
s = string[0]
alpha = string[1]

length = len(s)
start_idx = -1

for i in range(length - 1):
    if s[i] == alpha:
        start_idx = i
        break
print(start_idx)

if start_idx == -1:
    print("No")