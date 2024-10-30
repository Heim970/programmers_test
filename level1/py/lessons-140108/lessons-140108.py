# 프로그래머스 코딩테스트 연습 > 연습문제 > 문자열 나누기
# 2024-03-28

def solution(s):
    x_count = 0
    o_count = 0
    x = ''
    answer = 0
    
    for i in s:
        if x == '':
            x = i
            x_count = 1
        elif i == x:
            x_count += 1
        else:
            o_count += 1
            
        if x_count == o_count:
            x = ''
            x_count = 0
            o_count = 0
            answer += 1

    if x_count or o_count:
        answer += 1
        
    return answer