n = int(input())

for i in range(n):
    # 왼쪽 삼각형 부분
    for j in range(n - i):
        print("*", end="")
    # 가운데 공백 부분
    for j in range(2 * i):
        print(" ", end="")
    # 오른쪽 삼각형 부분
    for j in range(n - i):
        print("*", end="")
    print()