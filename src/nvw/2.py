from collections import deque

def solution(grid):
    r, c = len(grid), len(grid[0])
    pad = [[float('inf')] * c for _ in range(r)]
    q = deque([(0, 0)])
    pad[0][0] = grid[0][0]

    while q:
        x, y = q.popleft()

        if 0 <= x + 1 < r:
            if pad[x][y] + grid[x + 1][y] < pad[x + 1][y]:
                pad[x + 1][y] = pad[x][y] + grid[x + 1][y]
                q.append((x + 1, y))
        if 0 <= y + 1 < c:
            if pad[x][y] + grid[x][y + 1] < pad[x][y + 1]:
                pad[x][y + 1] = pad[x][y] + grid[x][y +1]
                q.append((x, y + 1))

    return pad[-1][-1]

if __name__ == '__main__':
    print(solution([ [1, 8, 3, 2], [7, 4, 6, 5] ]))