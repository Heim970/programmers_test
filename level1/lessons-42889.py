#프로그래머스 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율

def solution(N, stages):
    nc = {}
    cl = len(stages) #스테이지에 도달한 유저의 수
    for i in range(1, N+1):
        if cl != 0:
            nc.update({str(i): stages.count(i) / cl})
            cl -= stages.count(i)
        else:
            nc.update({str(i): 0}) #도달한 유저가 없는 경우 실패율 0

    nc = sorted(nc.items(), key=lambda x:x[1], reverse=True)
    return [int(i) for i, j in nc]
