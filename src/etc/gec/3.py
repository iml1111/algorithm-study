from collections import deque

def solution(N, bus_stop):
    answer = [[1300 for _ in range(N)] for _ in range(N)]
    bus_stop = [(x-1, y-1) for x,y in bus_stop]
    q = deque(bus_stop)
    for x,y in bus_stop:
        answer[x][y] = 0

    while q:
        x, y = q.popleft()
        for nx, ny in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
            if (
                0 <= nx < N and 0 <= ny < N
                and answer[nx][ny] > answer[x][y]
            ):
                answer[nx][ny] = answer[x][y] + 1
                q.append((nx, ny))
    return answer

if __name__ == '__main__':
    print(solution(
        3, [[1,2],[3,3]],
    ))