s = input()
leng = len(s)
cnt1 = 0
cnt2 = 0

for i in range(leng - 1):
    if s[i] == 'e' and s[i + 1] == 'e':
        cnt1 += 1
    if s[i] == 'e' and s[i + 1] == 'b':
        cnt2 += 1

print(cnt1, cnt2)