from pprint import pprint
from collections import deque

def is_way(node):
	return node not in {"1", "@"}

def get_start_idx(board, n, m):
	for idx in range(n):
		for jdx in range(m):
			if board[idx][jdx] == '3':
				return idx, jdx
	raise RuntimeError("3이 없음")


def solution(board):
	board = [list(i) for i in board]
	N, M = len(board), len(board[0])
	x, y = get_start_idx(board, N, M)
	q = deque([(x,y)])
	key, box = False, False
	while q:
		x, y = q.popleft()

		if 0 < x and is_way(board[x-1][y]):
			q.append((x-1, y))
		if 0 < y and is_way(board[x][y-1]):
			q.append((x, y-1))
		if x < N - 1 and is_way(board[x+1][y]):
			q.append((x+1, y))
		if y < M - 1 and is_way(board[x][y+1]):
			q.append((x, y+1))

		box = board[x][y] == '2' if not box else box
		key = board[x][y] == '4' if not key else key
		if box and key:
			return 1

		board[x][y] = '@'

	return 0

		


if __name__ == '__main__':
	print(solution(
		[
			"001020",
			"101000",
			"001110",
			"030100",
			"400000",
		]
	))
	print(solution(
		[
			"001020",
			"101000",
			"001110",
			"030100",
			"400100",
		]
	))