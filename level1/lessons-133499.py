# 프로그래머스 코딩테스트 연습 > 연습문제 > 옹알이(2)

def solution(babbling):
    answer = 0
    
    for word in babbling:
        for i in ["aya", "ye", "woo", "ma"]:
            if i*2 not in word:
                word = word.replace(i, " ", 1)
        if not word.strip():
            answer += 1
            
    return answer