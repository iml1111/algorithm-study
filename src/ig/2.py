import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(n, m, people):
    building = defaultdict(deque())
    elevator, next_floor = 1, 1
    pass

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, m, t = map(int, input().split())
        people = []
        for _ in range(t):
            src, tgt = map(int, input().split())
            people.append((src, tgt))
        solution(n, m, people)

"""
탑승 대기 층과 목적지 층이 같은 승객은 실제로 탑승하지 않는다고 명시되어 있는데,
아래 데이터는 2개가 같은 승객이지 않나요?
2
5 4 4
5 5 <<
...
"""