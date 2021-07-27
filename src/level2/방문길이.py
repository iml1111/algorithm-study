def solution(dirs):
    visited = set()
    d = {'U':(1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    move = lambda i, j, direc: (i + d[direc][0], j + d[direc][1])
    point = 0, 0
    for dir in dirs:
        next_point = move(*point, dir)
        if -5 <= next_point[0] <= 5 and -5 <= next_point[1] <= 5:
            visited.add((point, next_point))
            visited.add((next_point, point))
            point = next_point
    return len(visited) // 2


if __name__ == '__main__':
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))