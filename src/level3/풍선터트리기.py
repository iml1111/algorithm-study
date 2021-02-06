from collections import deque

def make_mins(a, min1=float('inf'), min2=float('inf')):
    pre_mins, post_mins = deque(), deque()
    for i in range(len(a)-2):
        min1 = min(min1, a[i])
        pre_mins.append(min1)
    for i in range(len(a)-2, 0, -1):
        min2 = min(min2, a[i])
        post_mins.appendleft(min2)
    return pre_mins, post_mins

def solution(a, answer=2):
    pres, posts = make_mins(a)
    for i, pre, post in zip(range(1, len(a) - 1), pres, posts):
        answer += int(a[i] <= pre or a[i] <= post)
    return answer

if __name__ == '__main__':
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))