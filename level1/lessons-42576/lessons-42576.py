# 코딩테스트 연습 > 해시 > 완주하지 못한 선수
# 2024-04-03
# 해시 사용 안함

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
