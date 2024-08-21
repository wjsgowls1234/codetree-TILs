string = input().split()
s = string[0]
alpha = string[1]

length = len(s)
start_idx = -1

for i in range(length):
    if s[i] == alpha:
        start_idx = i
        break
    if start_idx == -1:
        start_idx = "No"
print(start_idx)