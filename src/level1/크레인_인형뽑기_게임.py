'''
2019 카카오 개발자 겨울 인턴십
- 크레인 인형뽑기 게임 
'''

def get_stack_points(board, w, h):
    stacks = []
    for j in range(w):
        for i in range(h):
            if board[i][j]:
                stacks.append(i)
                break
    return stacks


def solution(board, moves):
    answer = 0
    w, h = len(board[0]), len(board)
    stacks = get_stack_points(board, w, h)
    bucket = []
    
    for move in moves:
        move = move - 1
        if stacks[move] < h:
            item = board[stacks[move]][move]
            if bucket and item == bucket[-1]:
                bucket.pop()
                answer += 2
            else:
                bucket.append(item)
            stacks[move] += 1
    
    return answer


if __name__ == '__main__':
    board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
    moves = [1,5,3,5,1,2,1,4]

    result = solution(board, moves)
    print(result)