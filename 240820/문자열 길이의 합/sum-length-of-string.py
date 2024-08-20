n = int(input())
leng = 0
all_len = 0
cnt = 0
all_cnt = 0

for _ in range(n):
    string = input()
    leng = len(string)
    all_len += leng
    cnt = string[0].count('a')
    all_cnt += cnt

print(all_len, all_cnt)