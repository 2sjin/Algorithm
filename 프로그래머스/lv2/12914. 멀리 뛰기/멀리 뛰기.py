def solution(n):
    df = [0 for _ in range(n+1)]
    df[0:2] = [1, 1]
    
    for i in range(2, n+1):
        df[i] = df[i-2] + df[i-1]

    return df[n] % 1234567