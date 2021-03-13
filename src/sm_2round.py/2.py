
def start(arr, max_step, start):
    steps = set()
    while start not in steps and len(steps) > max_step[start]:
        steps.add(start)
        max_step[start] = len(steps)
        start += arr[start]
    return len(steps) - max_step[start]

def solution(arr):
    answer = 0
    max_step = [-1 for _ in range(len(arr))]
    for i in range(3):
        answer = max(answer, start(arr, max_step, i))
    return answer + 1


if __name__ == '__main__':
    print(solution([3,5,-1,-2,4,4,3,-2,-3,-2]))
    print(solution([3, 5, -1, -2, 4, 4, 3, 1, -3, -2]))