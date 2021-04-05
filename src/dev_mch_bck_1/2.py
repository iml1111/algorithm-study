def make_board(rows, columns):
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1
    return board

def rotate(board, query):
    s_i, e_i, s_j, e_j = query[0], query[2], query[1], query[3]
    nums, maps, flag = [], [], 0
    i, j = s_i, s_j
    while not (flag == 3 and i == s_i and j == s_j):
        nums.append(board[i][j])
        maps.append((i, j))

        if flag == 0:
            if j + 1 <= e_j:
                j += 1
            else:
                flag = 1
                i += 1

        elif flag == 1:
            if i + 1 <= e_i:
                i += 1
            else:
                flag = 2
                j -= 1

        elif flag == 2:
            if s_j <= j - 1:
                j -= 1
            else:
                flag = 3
                i -= 1

        elif flag == 3:
            i -= 1

    for (i, j), num in zip(maps[1:] + [maps[0]], nums):
        board[i][j] = num

    return min(nums)


def solution(rows, columns, queries):
    board = make_board(rows, columns)
    answer = []
    for query in queries:
        query = (query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1)
        min_value = rotate(board, query)
        answer.append(min_value)
    return answer

if __name__ == '__main__':
    #print(solution(6, 6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    print((solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])))