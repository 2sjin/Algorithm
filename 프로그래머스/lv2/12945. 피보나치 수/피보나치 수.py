def solution(n):
    fibo = [0 for _ in range(n+1)]
    fibo[0:2] = [0, 1]
    
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    
    return fibo[n] % 1234567