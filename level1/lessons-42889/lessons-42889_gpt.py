#프로그래머스 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율
#GPT 첨삭버전

def solution(N, stages):
    failure_rate = []
    total_players = len(stages)
    
    for i in range(1, N+1):
        if total_players != 0:
            fail_count = stages.count(i)
            failure_rate.append((i, fail_count / total_players))
            total_players -= fail_count
        else:
            failure_rate.append((i, 0))
    
    failure_rate.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in failure_rate]
