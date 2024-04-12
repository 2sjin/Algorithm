# 벨트의 칸
class BeltPart:
    def __init__(self, life):
        self.life = life    # 내구도
        self.is_robot = False

# 벨트
class Belt:
    def __init__(self):
        self.parts = [BeltPart(life_input_list[i]) for i in range(2*n)]
        self.num_robot_put = 0
        self.num_robot_take = n-1

    # 벨트 회전
    def rotate(self):
        parts_end = self.parts[-1]
        for i in range(len(self.parts)-2, -1, -1):
            self.parts[i+1] = self.parts[i]
        self.parts[0] = parts_end

    # 로봇 이동
    def move_robot(self):
        for i in range(self.num_robot_take-1, self.num_robot_put-1, -1):
            # 조건: 현재 칸에 로봇이 없으면 생략
            if not self.parts[i].is_robot:
                continue

            # 조건: 이동할 칸에 로봇이 있으면 생략
            if self.parts[i+1].is_robot:
                continue

            # 조건: 이동할 칸의 내구도가 1 미만이면 생략
            if self.parts[i+1].life < 1:
                continue

            # 로봇 이동하고 내구도 1 감소
            self.parts[i].is_robot = False
            self.parts[i+1].is_robot = True
            self.parts[i+1].life -= 1

    # 로봇 올리기
    def put_robot(self):
        # 조건: 내구도 1 이상
        if self.parts[self.num_robot_put].life >= 1:
            self.parts[self.num_robot_put].is_robot = True
            self.parts[self.num_robot_put].life -= 1

    # 로봇 내리기
    def take_robot(self):
        self.parts[self.num_robot_take].is_robot = False

    # 작업을 계속 진행할지 여부를 반환
    def check_continue(self):
        life_zero_cnt = [part.life for part in self.parts].count(0)
        if life_zero_cnt < k:
            return True
        return False

# 입력
n, k = map(int, input().split())
life_input_list = list(map(int, input().split()))

# 벨트 객체 생성
belt = Belt()

# 작업 반복
cnt = 0
while belt.check_continue():
    cnt += 1
    belt.rotate()
    belt.take_robot()
    belt.move_robot()
    belt.take_robot()
    belt.put_robot()

# 디버깅 출력
print(cnt)