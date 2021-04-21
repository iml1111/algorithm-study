import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline


def solution(n, cost):
    time, cnt, heap,  = 0, 0, [(i, i) for i in cost]
    heapify(heap)
    while cnt < n:
        time, cost_i = heappop(heap)
        heappush(heap, (time + cost_i, cost_i))
        cnt += 1
    return time

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, _ = map(int, input().split())
        cost = list(map(int, input().split()))
        print(solution(n, cost))

    #print(solution(5, [12, 10, 4]))
    #print(solution(3, [3,100,3]))
    #print(solution(3, [1, 100, 100]))