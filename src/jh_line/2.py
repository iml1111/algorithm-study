def solution(arr):
	stack, answer = [0], {}

	for i in range(1, len(arr)):
		while stack and arr[stack[-1]] < arr[i]:
			target = stack.pop()
			if arr[target] not in answer:
				answer[arr[target]] = i
		if stack and arr[stack[-1]] > arr[i]:
			answer[arr[i]] = stack[-1]
		stack.append(i)
	
	return [answer[i] if i in answer else -1 for i in arr]


if __name__ == '__main__':
	print(solution([3,5,4,1,2]))
	print(solution([1,2,3,4,5]))
	print(solution([5,4,3,2,1]))
	print(solution([2,5,3,4,1]))
	print(solution([2,5,4,3,1]))
	print(solution([1,3,5,7,9]))
	'''
	[1, -1, 1, 2, 2]
[1, 2, 3, 4, -1]
[-1, 0, 1, 2, 3]
[1, -1, 1, 1, 3]
'''