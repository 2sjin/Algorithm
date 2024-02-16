
# 토네이도 클래스
class Tornado:
    def __init__(self, row, col):
        self.row = row          # 토네이도 위치(행)
        self.col = col          # 토네이도 위치(열)
        self.direction = 9      # 토네이도 이동 방향(3/6/9/12시)
        self.rotate_cnt = 0     # 토네이도 회전 횟수

    # 토네이도 이동(1칸)
    def move(self): 
        if self.direction == 3:
            self.col += 1
        elif self.direction == 6:
            self.row += 1
        elif self.direction == 9:
            self.col -= 1
        elif self.direction == 12:
            self.row -= 1

    # 토네이도 회전(반시계 방향)
    def rotate(self):
        if self.direction == 3:
            self.direction = 12
        else:
            self.direction -= 3
        self.rotate_cnt += 1


# grid 내 특정 좌표에 모래 양을 더하는 함수
def add_sand(row, col, value):
    global grid, outside_sand, n

    # 좌표가 격자 범위에 해당하면 모래 양 더하기
    if (0 <= row < n and 0 <= col < n):
        grid[row][col] += value

    # 격자 범위를 벗어나는 모래는 별도 합산
    else:
        outside_sand += value

# 격자 내 모래 이동(방향에 따라)
# 토네이도를 먼저 이동한 뒤에 이 함수 호출하기
def move_sand():
    global grid, tornado

    tr = tornado.row
    tc = tornado.col
    t_direction = tornado.direction

    # 현재 토네이도 위치의 모래 양
    sand_y = grid[tr][tc]

    # a 칸으로 이동할 모래 양 미리 계산해놓기
    sand_move_a = sand_y
    sand_move_a -= int(sand_y * 0.01)
    sand_move_a -= int(sand_y * 0.01)
    sand_move_a -= int(sand_y * 0.07)
    sand_move_a -= int(sand_y * 0.07)
    sand_move_a -= int(sand_y * 0.02)
    sand_move_a -= int(sand_y * 0.02)
    sand_move_a -= int(sand_y * 0.10)
    sand_move_a -= int(sand_y * 0.10)
    sand_move_a -= int(sand_y * 0.05)

    # 분기: 3시 방향인 경우
    if t_direction == 3:
        add_sand(tr-1, tc-1, int(sand_y * 0.01))
        add_sand(tr+1, tc-1, int(sand_y * 0.01))
        add_sand(tr-1, tc, int(sand_y * 0.07))
        add_sand(tr+1, tc, int(sand_y * 0.07))
        add_sand(tr-2, tc, int(sand_y * 0.02))
        add_sand(tr+2, tc, int(sand_y * 0.02))
        add_sand(tr-1, tc+1, int(sand_y * 0.10))
        add_sand(tr+1, tc+1, int(sand_y * 0.10))
        add_sand(tr, tc+2, int(sand_y * 0.05))
        add_sand(tr, tc+1, sand_move_a)

    # 분기: 6시 방향인 경우
    elif t_direction == 6:
        add_sand(tr-1, tc-1, int(sand_y * 0.01))
        add_sand(tr-1, tc+1, int(sand_y * 0.01))
        add_sand(tr, tc-1, int(sand_y * 0.07))
        add_sand(tr, tc+1, int(sand_y * 0.07))
        add_sand(tr, tc-2, int(sand_y * 0.02))
        add_sand(tr, tc+2, int(sand_y * 0.02))
        add_sand(tr+1, tc-1, int(sand_y * 0.10))
        add_sand(tr+1, tc+1, int(sand_y * 0.10))
        add_sand(tr+2, tc, int(sand_y * 0.05))
        add_sand(tr+1, tc, sand_move_a)
    
    # 분기: 9시 방향인 경우
    elif t_direction == 9:
        add_sand(tr-1, tc+1, int(sand_y * 0.01))
        add_sand(tr+1, tc+1, int(sand_y * 0.01))
        add_sand(tr-1, tc, int(sand_y * 0.07))
        add_sand(tr+1, tc, int(sand_y * 0.07))
        add_sand(tr-2, tc, int(sand_y * 0.02))
        add_sand(tr+2, tc, int(sand_y * 0.02))
        add_sand(tr-1, tc-1, int(sand_y * 0.10))
        add_sand(tr+1, tc-1, int(sand_y * 0.10))
        add_sand(tr, tc-2, int(sand_y * 0.05))
        add_sand(tr, tc-1, sand_move_a)
        
    # 분기: 12시 방향인 경우
    elif t_direction == 12:
        add_sand(tr+1, tc-1, int(sand_y * 0.01))    
        add_sand(tr+1, tc+1, int(sand_y * 0.01))
        add_sand(tr, tc-1, int(sand_y * 0.07))
        add_sand(tr, tc+1, int(sand_y * 0.07))
        add_sand(tr, tc-2, int(sand_y * 0.02))
        add_sand(tr, tc+2, int(sand_y * 0.02))
        add_sand(tr-1, tc-1, int(sand_y * 0.10))
        add_sand(tr-1, tc+1, int(sand_y * 0.10))
        add_sand(tr-2, tc, int(sand_y * 0.05))
        add_sand(tr-1, tc, sand_move_a)

    # 현재 토네이도 위치의 모래 양을 0으로
    grid[tr][tc] = 0


# 입력(격자 크기)
n = int(input())

# 입력(격자 생성)
grid = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    grid[i] = row

# 토네이도 객체 생성
tornado = Tornado(n//2, n//2)

# 격자 밖으로 나간 모래 양
outside_sand = 0

# 반복
while True:
    # 토네이도가 두 번 회전할 때마다 이동 반복 횟수 1씩 증가
    move_repeat_cnt = (tornado.rotate_cnt // 2) + 1

    # 토네이도를 같은 방향으로 반복 이동
    for i in range(move_repeat_cnt):
        # 토네이도 이동(1칸)
        tornado.move()
    
        # 격자 내 모래 이동(방향에 따라)
        # 격자 밖으로 나간 모래 양은 별도로 합산하기
        move_sand()

        # [디버깅 코드] 격자 출력
        # print("(", tornado.row, ",", tornado.col, ")")
        # for rr in range(n):
        #     for cc in range(n):
        #         print(grid[rr][cc], end=" ")
        #     print()
        # print()

        # 토네이도가 위치가 (0, 0)이면 이동 종료
        if tornado.row == 0 and tornado.col == 0:
            break

    # 토네이도가 위치가 (0, 0)이면 반복문 탈출
    if tornado.row == 0 and tornado.col == 0:
        break

    # 토네이도 회전(반시계 방향)
    tornado.rotate()


# 출력
print(outside_sand)
