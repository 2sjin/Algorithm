m, n = map(int, input().split())

grid = [[0 for _ in range(n)] for _ in range(m)]

movement = ((0, 1), (1, 0), (0, -1), (-1, 0))
movement_type = 0

snail_row = 0
snail_col = 0

result = 0

# 초기 위치 방문 처리
grid[0][0] = 1

for i in range(m*n):
    # 이동 지점 확인
    search_row = snail_row + movement[movement_type][0]
    search_col = snail_col + movement[movement_type][1]

    # 이동 지점이 표 밖에 있으면 방향 전환
    if not (0 <= search_row < m and 0 <= search_col < n):
        movement_type = (movement_type + 1) % 4
        result += 1

    # 또는 이동 지점이 이미 방문한 곳이면 방향 전환
    elif grid[search_row][search_col] == 1:
        movement_type = (movement_type + 1) % 4
        result += 1

    # 이동
    snail_row += movement[movement_type][0]
    snail_col += movement[movement_type][1]

    # 방문 처리
    grid[snail_row][snail_col] = 1

print(result - 1)
