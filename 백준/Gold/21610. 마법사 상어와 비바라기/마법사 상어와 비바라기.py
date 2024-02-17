# 구름 클래스
class Cloud:
    def __init__(self, row, col):
        self.row = row               # 좌표(행)
        self.col = col               # 좌표(열)

    # 구름 이동
    def move(self, direction, speed):
        # 9시 방향
        if direction == 1:
            self.col -= speed
        # 11시 방향
        if direction == 2:
            self.row -= speed
            self.col -= speed
        # 12시 방향
        if direction == 3:
            self.row -= speed
        # 1시 방향
        if direction == 4:
            self.row -= speed
            self.col += speed
        # 3시 방향
        if direction == 5:
            self.col += speed
        # 5시 방향
        if direction == 6:
            self.row += speed
            self.col += speed
        # 6시 방향
        if direction == 7:
            self.row += speed
        # 7시 방향
        if direction == 8:
            self.row += speed
            self.col -= speed

        # 무한루프 보정
        if not (0 <= self.row < n):
            self.row = self.row % n
        if not (0 <= self.col < n):
            self.col = self.col % n

# 입력
n, m = map(int, input().split())

# 격자 생성
grid = [[] for _ in range(n)]
for i in range(n):
    grid[i] = list(map(int, input().split()))

# 구름 초기 생성
cloud_list = [None for _ in range(4)]
for i in range(4):
    cloud_list[0] = Cloud(n-1, 0)
    cloud_list[1] = Cloud(n-1, 1)
    cloud_list[2] = Cloud(n-2, 0)
    cloud_list[3] = Cloud(n-2, 1)

# 구름 이동 반복
for _ in range(m):
    # 구름 이동 정보 입력
    d, s = map(int, input().split())

    # 구름 이동
    for cloud in cloud_list:
        # 현재 위치에서 d 방향으로 s칸 이동
        cloud.move(d, s)

        # 현재 위치에 물의 양 +1
        grid[cloud.row][cloud.col] += 1

    # 구름 소멸 전, 위치 확인을 위한 백업
    cloud_pos_backup = [(cloud.row, cloud.col) for cloud in cloud_list]

    # 구름 소멸 
    cloud_list = []

    # 물복사버그 마법 시전
    # 대각선 4방향 중 물이 있는 칸 수 만큼, 현재 위치에 물의 양 더하기
    for cloud_row, cloud_col in cloud_pos_backup:
        # 대각선에 물이 있는 바구니가 몇개인지 체크(무한루프 적용 X)
        movement = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        is_water_cnt = 0
        for mr, mc in movement:
            if 0 <= cloud_row+mr < n and 0 <= cloud_col+mc < n:
                if grid[cloud_row+mr][cloud_col+mc] > 0:
                    is_water_cnt += 1
        # 물의 양 더하기
        grid[cloud_row][cloud_col] += is_water_cnt

    # 새로운 구름 생성
    for i in range(n):
        for j in range(n):
            # 물의 양이 2 이상
            if grid[i][j] >= 2:
                # 구름이 사라진 칸이 아닌 경우
                if (i, j) not in cloud_pos_backup:
                    # 구름 생성, 물의 양 2 감소
                    cloud_list.append(Cloud(i, j))    # 구름 생성
                    grid[i][j] -= 2                   # 물의 양 -2

# 출력
result = 0
for row in grid:
    result += sum(row)
print(result)
            
