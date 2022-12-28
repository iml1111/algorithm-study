def solution(a_path: str, b_path: str):
	lcs = [[0 for _ in range(len(b_path) + 1)] for _ in range(len(a_path) + 1)]
	
	max_value, max_idx, max_str = 0, (0, 0), ""
	for i in range(1, len(a_path) + 1):
		for j in range(1, len(b_path) + 1):
			if a_path[i - 1] == b_path[j - 1]:
				lcs[i][j] = lcs[i - 1][j - 1] + 1
				if max_value < lcs[i][j]:
					max_value = lcs[i][j]
					max_idx = (i, j)
	
	for idx in range(max_idx[0] - 1, max_idx[0] - max_value - 1, -1):
		max_str += a_path[idx]

	return max_value, max_str[::-1]

if __name__ == '__main__':
	print(solution(
		"ACIABCIKQM",
		"ALABCEFG",
	))
	print(solution(
		"TELEVISION",
		"TELEPHONES",
	))