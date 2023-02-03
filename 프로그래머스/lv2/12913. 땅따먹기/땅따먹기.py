def solution(land):
    row = len(land)
    col = len(land[0])
    
    dp = [[0] * col for i in range(row)]
    dp[0] = land[0]
    
    for i in range(1, row):
        for j in range(col):
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i][j]
    
    return max(dp[-1])