# 코딩테스트 연습 > 탐욕법(Greedy) > 체육복
# 2024-04-02

def solution1(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    tl = [] # 여분도 없고, 체육복을 잃어버린 학생
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer += 1
        else:
            tl.append(i)

    for i in tl:
        if i - 1 in reserve:
            reserve.remove(i-1)
            answer += 1
                
        elif i + 1 in reserve:
            reserve.remove(i+1)
            answer += 1
        
    return answer


# GPT 코드, 일부수정

def solution2(n, lost, reserve):
    lost_set = set(lost) - set(reserve)  # reserve에 없는 학생만 남깁니다.
    reserve_set = set(reserve) - set(lost)  # lost에 없는 학생만 남깁니다.
    answer = n - len(lost_set)
    
    for i in lost_set:
        if i - 1 in reserve_set:
            reserve_set.remove(i - 1)
            answer += 1
        elif i + 1 in reserve_set:
            reserve_set.remove(i + 1)
            answer += 1

    return answer