"""
input_pad는 반드시 직사각형의 형태로 온다고 전제합니다.
"""
def refine_pad(input_pad):
	pad = []
	area_id, vertical_set = 0, set()
	i_len, j_len = len(input_pad), len(input_pad[0])

	for i in range(j_len):
		for j in range(i_len):
			if input_pad[j][i] == '#':
				area_id += 1
			else:
				input_pad[j][i] = area_id
				vertical_set.add(area_id)
		area_id += 1

	area_id = 0
	for i in range(i_len):
		for j in range(j_len):
			if input_pad[i][j] == '#':
				area_id += 1
			else:
				pad.append([area_id, input_pad[i][j]])
		area_id += 1

	pad_len, max_horizon = len(pad), pad[-1][0]
	next_horizon = pad_len - 1
	for i in range(pad_len - 1, -1, -1):
		if i + 1 < pad_len - 1 and  pad[i][0] != pad[i + 1][0]:
			next_horizon = i + 1
		pad[i].append(next_horizon)

	return pad, pad_len, max_horizon, len(vertical_set)


def solution(input_pad):
	p_num, case = 0, 0
	pad, pad_len, last_horizon, max_verticals_len = refine_pad(input_pad)

	def tracking(num, start_i, horizon, verticals, vertical_len):
		nonlocal p_num, case, pad, pad_len, last_horizon, max_verticals_len
		if horizon < last_horizon and vertical_len < max_verticals_len:
			for i in range(start_i, pad_len):
				h, v, next_i = pad[i]
				if v not in verticals:
					tracking(num+1, next_i, h, verticals+[v], vertical_len+1)
		elif p_num < num:
			p_num, case = num, 1
		elif p_num == num:
			case += 1

	tracking(0, 0, -1, [], 0)
	return f"최대 {p_num}명, {case}가지"


if __name__ == '__main__':
	import time
	# 벽 = #, 길 = O
	print(solution([
		["O", "O", ],
		["O", "O", ],
	]))
	print(solution([
	    ["#","#","#","O",],
	    ["O","O","O","O",],
	    ["O","#","O","O",],
	    ["#","#","#","O",],
	]))
	print(solution([
		["O", "O", "O", "O", ],
		["O", "O", "O", "O", ],
		["O", "O", "O", "O", ],
		["O", "O", "O", "O", ],
	]))
	print(solution([
		["O","O","O","#","O","O","O","O",],
		["O","O","O","O","O","#","O","#",],
		["O","#","O","O","O","O","O","O",],
		["O","O","O","O","#","O","#","O",],
	]))
	start = time.time()
	print(solution([
		["O","#", "O", "#", "O", "#", "O", "#"],
		["O","O", "O", "O", "O", "#", "O", "O"],
		["#","O", "#", "O", "O", "#", "O", "#"],
		["O","O", "O", "O", "O", "O", "O", "O"],
	    ["O","O", "O", "#", "O", "O", "O", "O"],
	    ["O","O", "O", "O", "O", "#", "O", "#"],
	    ["O","#", "O", "O", "O", "O", "O", "O"],
	    ["O","O", "O", "O", "#", "O", "#", "O"],
	]))
	print("time:", time.time() - start)
	"""
	최대 2명, 2가지
	최대 4명, 2가지
	최대 4명, 24가지
	최대 9명, 33가지
	최대 15명, 560가지
	"""