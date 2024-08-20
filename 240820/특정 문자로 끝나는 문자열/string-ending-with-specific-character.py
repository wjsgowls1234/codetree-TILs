string = [
    input()
    for _ in range(10)
]
alpha = input()
cnt = 0

for i in range(10):
    if string[i][-1] == alpha:
        cnt += 1
        print(string[i])
    
if cnt == 0:
    print("None")