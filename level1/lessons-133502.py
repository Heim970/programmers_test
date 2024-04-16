# 프로그래머스 코딩테스트 연습 > 연습문제 > 햄버거 만들기
# 2024-04-16

def solution(ingredient):
    answer = 0
    tmp = ''
    for i in ingredient:
        tmp += str(i)
        if tmp[-4:] == "1231":
            answer += 1
            tmp = tmp[:-4]
    return answer