M, N = map(int, input().split())

arr = list(range(1, M+1))

for _ in range(N):
    i, j = map(int, input().split())

    start = i-1
    end = j
    arr_temp = arr[start:end]
    arr_temp.reverse()

    cnt = 0
    for idx in range(i-1, j):
        arr[idx] = arr_temp[cnt]
        cnt += 1

for x in arr:
    print(x, end=" ")
