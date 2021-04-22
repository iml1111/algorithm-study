import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def solution(n, m, people):
    people = list(reversed(people))
    building, building_num = defaultdict(deque), 0
    elevator, elevator_num = defaultdict(int), 0
    max_elevator_num = elevator_num
    cur_floor, next_floor = 1, 1
    time = 1
    while people or building_num:

        if people: # 엘레베이터 대기 인원 추가
            src, tgt = people.pop()
            if src != tgt:
                building[src].append(tgt)
                building_num += 1

        # 현재 층이 도착지인 사람 모두 하차
        if cur_floor in elevator:
            elevator_num -= elevator[cur_floor]
            del elevator[cur_floor]

        # 현재 층 대기 인원 1명 탑승
        if cur_floor in building:
            if elevator_num < m:
                tgt = building[cur_floor].popleft()
                building_num -= 1
                if not building[cur_floor]:
                    del building[cur_floor]
                elevator[tgt] += 1
                elevator_num += 1
            else:
                return time

        max_elevator_num = max(max_elevator_num, elevator_num)
        time += 1
        cur_floor += next_floor
        if cur_floor in {1, n}:
            next_floor *= -1

    return -max_elevator_num


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, m, t = map(int, input().split())
        people = []
        for _ in range(t):
            src, tgt = map(int, input().split())
            people.append((src, tgt))
        print(solution(n, m, people))
    # print(solution(5, 4, [(5, 5),(2, 5),(3, 4),(5, 4),]))
    # print(solution(3, 1, [(1,3), (2, 3)]))
    # print(solution(
    #     5, 3,
    #     [(1, 5), (2, 5), (3, 4), (4, 5), (5, 1),
    #      (3, 5), (2, 5), (1, 5), (2, 5)]
    # ))
