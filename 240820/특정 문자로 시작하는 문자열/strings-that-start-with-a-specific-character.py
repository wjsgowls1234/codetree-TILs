n = int(input())
string = [
    input()
    for _ in range(n)
]
alpha = input()
cnt = 0
len_all = 0

for i in range(n):
    if string[i][0] == alpha:
        cnt += 1
        len_all += len(string[i])
print(cnt, f"{len_all / cnt :.2f}")