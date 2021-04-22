WALL, ROUTE  = '#', 'O'


def get_area(i, j, pad):
	area_set = {(i, j)}
	
	point = 1
	while 0 <= i - point and \
	pad[i - point][j] == ROUTE:
		area_set.add((i - point, j))
		point += 1

	point = 1
	while 0 <= j - point and \
	pad[i][j - point] == ROUTE:
		area_set.add((i, j - point))
		point += 1

	point = 1
	while i + point < len(pad) and \
	pad[i + point][j] == ROUTE:
		area_set.add((i + point, j))
		point += 1

	point = 1
	while j + point < len(pad[0]) and \
	pad[i][j + point] == ROUTE:
		area_set.add((i, j + point))
		point += 1

	return area_set


def tracking(num, s_i, s_j, area_set, pad, stack):
	p_num, case = num, 1
	for i in range(s_i, len(pad)):
		for j in range(s_j if i == s_i else 0, len(pad[0])):
			if (
				pad[i][j] == ROUTE and 
				(i, j) not in area_set
			):
				p_num_i, case_i = tracking(
					num + 1, i, j,
					area_set | get_area(i, j, pad),
					pad,
					stack + [(i, j)]

				)
				if p_num == p_num_i:
					case += case_i
				elif p_num < p_num_i:
					p_num = p_num_i
					case = case_i

	return (p_num, case)


def solution(pad):
	for i in range(len(pad)):
		for j in range(len(pad[0])):
			if pad[i][j] == ROUTE:
				return "최대 %s명, %s가지" % tracking(0, 0, 0, set(), pad, [])



if __name__ == '__main__':
    print(solution([
        "OOO#OOOO",
        "OOOOO#O#",
        "O#OOOOOO",
        "OOOO#O#O",
    ]))
    # print(solution([
    #     "###O",
    #     "OOOO",
    #     "O#OO",
    #     "###O",
    # ]))
    # print(solution([
    #     "OO",
    #     "OO",
    # ]))
