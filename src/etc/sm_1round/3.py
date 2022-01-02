from bisect import  bisect
from collections import deque

def solution(pinuts, target_num, pos):
    pos_cur = bisect(pinuts, pos)
    left_cur, right_cur = pos, pos
    answer, cur_num = 0, 0

    q = deque(list(reversed(pinuts[:pos_cur])) + list(reversed(pinuts[pos_cur:])))
    while q and cur_num < target_num:
        left = abs(q[0] - left_cur)
        right = abs(q[-1] - right_cur)
        if left < right:
            left_cur = q.popleft()
            answer += left
        else:
            right_cur = q.pop()
            answer += right
        cur_num += 1

    return answer

if __name__ == '__main__':
    print(
        solution(
            [2,4,5,8,11,12], 3, 7
        )
    )