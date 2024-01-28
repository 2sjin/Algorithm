def dfs(graph, visited, com):
    # 현재 컴퓨터 방문 처리
    visited[com] = True

    # 인접 컴퓨터 방문
    for i in graph[com]:
        if not visited[i]:
            dfs(graph, visited, i)

def solution(n, computers):
    # 컴퓨터별 방문 여부
    visited = [False] * n
    
    # computers를 딕셔너리로 표현하기
    # 예: 컴퓨터 1이 0, 2와 연결되었으면 1: [0, 2]
    dic = {}
    for i in range(n):
        dic[i] = []
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                dic[i].append(j)
    
    # 컴퓨터 0부터 n-1까지 DFS 탐색
    # 단, 이미 탐색(방문)한 컴퓨터는 생략
    result = 0
    for i in range(n):
        if not visited[i]:
            dfs(dic, visited, i)
            result += 1
    
    return result