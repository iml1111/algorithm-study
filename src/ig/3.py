"""
input_pad는 반드시 직(정)사각형의 형태로 온다고 전제합니다.
벽 = #, 길 = O
"""

def refine_pad(input_pad):
	pad = []
	area_id = 0
	for i in range(len(input_pad[0])):
		for j in range(len(input_pad)):
			if input_pad[j][i] == '#':
				area_id += 1
			else:
				input_pad[j][i] = area_id
		area_id += 1
	area_id = 0
	for i in range(len(input_pad)):
		for j in range(len(input_pad[0])):
			if input_pad[i][j] == '#':
				area_id += 1
			else:
				pad.append((area_id, input_pad[i][j]))
		area_id += 1
	return pad


def tracking(
	num, start_i,
	max_horizon_num, vertical_area, pad
):
	p_num, case = num, 1
	for i in range(start_i, len(pad)):
		if pad[i][0] > max_horizon_num and pad[i][1] not in vertical_area:
			p_num_i, case_i = tracking(
				num + 1, i + 1,
				pad[i][0],
				vertical_area | {pad[i][1]},
				pad
			)
			if p_num < p_num_i:
				p_num, case = p_num_i, case_i
			elif p_num == p_num_i:
				case += case_i

	return (p_num, case)


def solution(input_pad):
	return "최대 %s명, %s가지" % tracking(
		0, 0, -1, set(), refine_pad(input_pad)
	)


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
