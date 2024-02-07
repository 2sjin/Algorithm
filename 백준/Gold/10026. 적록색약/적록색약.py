import sys
from sys import stdin

sys.setrecursionlimit(10**6)

movement = ((-1, 0), (1, 0), (0, -1), (0, 1))

# DFS
def dfs(row, col, graph, mark, rgb, weak):    
    # 방문 처리
    graph[row][col] = mark

    # 주변 4방향 방문(깊이 우선)
    for move in movement:
        m_row = row + move[0]
        m_col = col + move[1]

        # 범위를 벗어나면 통과
        if not (0 <= m_row < n and 0 <= m_col < n):
            continue

        # 이미 방문한 곳이면 통과
        if str(graph[m_row][m_col]) not in "RGB":
            continue

        # RGB가 같을 경우 DFS
        if graph[m_row][m_col] == rgb:
            dfs(m_row, m_col, graph, mark, rgb, weak)
            
        # 적록색약일 경우 R=G
        elif weak and str(graph[m_row][m_col]) + str(rgb) in ("RG", "GR"):
            dfs(m_row, m_col, graph, mark, rgb, weak)            

# 입력
n = int(stdin.readline().strip())

graph_normal = [[] for _ in range(n)]
graph_weak = [[] for _ in range(n)]

for i in range(n):
    graph_row = stdin.readline().strip()
    graph_normal[i] = list(graph_row)
    graph_weak[i] = list(graph_row)

# DFS 수행
mark_normal, mark_weak = 1, 1
for i in range(n):
    for j in range(n):
        if str(graph_normal[i][j]) in "RGB":
            dfs(i, j, graph_normal, mark_normal, graph_normal[i][j], weak=False)
            mark_normal += 1
        if str(graph_weak[i][j]) in "RGB":
            dfs(i, j, graph_weak, mark_weak, graph_weak[i][j], weak=True)
            mark_weak += 1
            
print(mark_normal-1, mark_weak-1)
