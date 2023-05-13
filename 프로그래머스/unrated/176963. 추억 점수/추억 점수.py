# 딕셔너리(이름-점수)
dic = {}
result = []

# 딕셔너리 key를 value로 반환
def key_to_value(k):
    try:
        return dic[k]
    except:         # 그리움 점수가 없으면
        return 0    # 0 반환

# 솔루션 함수
def solution(name, yearning, photo):
    # 딕셔너리에 (이름, 점수) 추가
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    # 사진 리스트의 이름(key)을 점수(value)로 변환,
    # 점수 합을 result 리스트에 추가
    for x in photo:
        result.append(sum(map(key_to_value, x)))
        
    # result 리스트 반환
    return result