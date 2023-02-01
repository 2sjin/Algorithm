def solution(triangle):
    df = []
    for i in range(1, len(triangle)+1):
        df.append([0] * i)

    df[0][0] = triangle[0][0]

    for i in range(1, len(df)):
        for j in range(len(df[i])):
            tmp_list = []
            if j-1 >= 0: tmp_list.append(df[i-1][j-1])
            if j < len(df[i])-1: tmp_list.append(df[i-1][j])
            df[i][j] = max(tmp_list) + triangle[i][j]
            
    return max(df[-1])