def solution(brown, yellow):
    tmp = (brown + 4) // 2      # 둘레의 절반
    for i in range(round(tmp/2), tmp):          # 둘레의 모든 경우의 수
        if i * (tmp-i) == brown + yellow:       # 넓이 확인(가로*세로 == 갈색+노란색)
            return [i, tmp-i]