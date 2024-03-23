# 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발 > 로또의 최고 순위와 최저 순위
# 2024-03-23

def solution(lottos, win_nums):
    wins = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    for i in lottos:
        if i == 0:
            wins[0] += 1
        elif i in win_nums:
            wins[0] += 1
            wins[1] += 1
        
    return [rank[wins[0]], rank[wins[1]]]