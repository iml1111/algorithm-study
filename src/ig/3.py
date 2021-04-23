"""
input_pad는 반드시 직(정)사각형의 형태로 온다고 전제합니다.
"""

def refine_pad(input_pad):
	area_id, init = 0, True
	start_i, start_j, last_i, last_j = 0, 0, 0, 0
	for i in range(len(input_pad)):
		for j in range(len(input_pad[0])):
			if input_pad[i][j] == '#':
				area_id += 1
			else:
				input_pad[i][j] = [area_id]
				if init:
					start_i, start_j, init = i, j, init
				last_i, last_j = i, j
		area_id += 1

	area_id = 0
	for i in range(len(input_pad[0])):
		for j in range(len(input_pad)):
			if input_pad[j][i] == '#':
				area_id += 1
			else:
				input_pad[j][i].append(area_id)
		area_id += 1

	return input_pad, start_i, start_j, input_pad[last_i][last_j]


def tracking(
	num, start_i, start_j,
	horizon_areas,
	vertical_areas,
	last_area, pad
):
	p_num, case = num, 1
	if last_area[0] not in horizon_areas or last_area[1] not in vertical_areas:
		for i in range(start_i, len(pad)):
			for j in range(start_j, len(pad[0])):
				if (
					pad[i][j] != '#' and
					pad[i][j][0] not in horizon_areas and
					pad[i][j][1] not in vertical_areas
				):
					p_num_i, case_i = tracking(
						num + 1, i, j + 1,
						horizon_areas | {pad[i][j][0]},
						vertical_areas | {pad[i][j][1]},
						last_area, pad
					)
					if p_num == p_num_i:
						case += case_i
					elif p_num < p_num_i:
						p_num, case = p_num_i, case_i
			start_j = 0

	return (p_num, case)


def solution(input_pad):
	pad, start_i, start_j, last_area = refine_pad(input_pad)
	return "최대 %s명, %s가지" % tracking(0, 0, 0, set(), set(), last_area, pad)


if __name__ == '__main__':
	import time
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
