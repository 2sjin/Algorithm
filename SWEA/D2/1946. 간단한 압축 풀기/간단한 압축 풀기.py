t = int(input())

for i in range(t):
    print("#" + str(i+1))
    n = int(input())  

    # 케이스별 문서 입력
    result = ""
    for _ in range(n):
        alpha, num = input().split()
        result += alpha * int(num)

    # 케이스별 문서 출력
    for idx, ch in enumerate(result):
        print(ch, end="")
        if idx % 10 == 9:
            print()

    print()