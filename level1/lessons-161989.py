# 프로그래머스 코딩 테스트 연습 Level 1. 덧칠하기 / Python3

def solution(n, m, section):
    if m == 1:
        return len(section)
    
    result = 1
    start = section[0]
    for i in range(1, len(section)):
        if start + m - 1 < section[i]:
            result += 1
            start = section[i]
            
    return result

# 테스트케이스
print(solution(8, 4, [2, 3, 6]) == 2)
print(solution(5, 4, [1, 3]) == 1)
print(solution(4, 1, [1, 2, 3, 4]) == 4)
print(solution(10, 3, [1, 7, 9, 10]) == 3)