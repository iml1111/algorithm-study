MAP = {
	'>': '<',
	'}': '{',
	']': '[',
	')': '('
}

def solution(string):
	if string[0] in MAP.keys():
		return 0

	stack, cnt = [], 0
	for idx, str_i in enumerate(string):
		if str_i in MAP.values():
			stack.append(str_i)
		elif str_i in MAP.keys():
			if stack and stack[-1] == MAP[str_i]:
				stack.pop()
				cnt += 1
			else:
				return -idx

	return -len(string) + 1 if stack else cnt

if __name__ == '__main__':
	print(solution("Hello, world!"))
	print(solution("line [({<plus>)}]"))
	print(solution("line [({<plus>})"))
	print(solution(">_<"))
	print(solution("x * (y + z) ^ 2 = ?"))