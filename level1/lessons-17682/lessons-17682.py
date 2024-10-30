# 프로그래머스 코딩테스트 연습 > 2018 kakao blind recruitment > [1차] 다트 게임
# 2024-03-19

def solution(dartResult):
    scores = []
    c_score = ''
    bonus = {"S": 1, "D": 2, "T": 3}
    
    for c in dartResult:
        # c가 숫자일 경우 점수로 저장
        if c.isdigit():
            c_score += c
        
        # 중간 점수 계산 후 scores 리스트에 저장    
        elif c in ["S", "D", "T"]:
            scores.append(int(c_score) ** bonus[c])
            c_score = ''
        
        # 점수의 보너스 옵션 적용
        elif c == "*":
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif c == "#":
            scores[-1] *= -1
            
    return sum(scores)