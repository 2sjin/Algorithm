from collections import deque

# 동서남북
movement = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(row, col, graph):
    # 큐 생성 및 초기 위치 push 
    queue = deque()
    queue.append((row, col))
    
    # 큐가 empty 될 때까지 반복
    while queue:
        # 큐 pop
        q_row, q_col = queue.popleft()
        
        # pop한 위치 인근 동서남북 탐색
        for m in movement:
            m_row = q_row + m[0]
            m_col = q_col + m[1]
            
            # 범위를 벗어나면 탐색 무시
            if not (0 <= m_row < len(graph) and 0 <= m_col < len(graph[0])):
                continue
            
            # 벽을 만나면 탐색 무시
            if graph[m_row][m_col] == 0:
                continue
                
            # 탐색하지 않은 곳 탐색하기
            if graph[m_row][m_col] == 1:
                graph[m_row][m_col] = graph[q_row][q_col] + 1
                # 탐색 위치를 큐에 push
                queue.append((m_row, m_col))
            
    # 맨 끝 좌표 리턴하기(단, 1인 경우 -1로)
    target = graph[len(graph)-1][len(graph[0])-1]
    return target if target != 1 else -1
        
def solution(maps):
    return bfs(0, 0, maps)