lst = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()
cnt = 0

for i in range(5):
    if lst[i][2] == a or lst[i][3] == a:
        cnt += 1
        print(lst[i])
print(cnt)