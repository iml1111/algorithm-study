from heapq import heappop, heappush, heapify

def solution(ads):
	wait, ads = 0, [[start, -cost] for start, cost in ads]
	heapify(ads)
	while ads:
		target, candidates = heappop(ads), []
		while ads and ads[0][0] < target[0] + 5:
			candidates.append(heappop(ads))
		end_time = target[0] + 5
		for cand in candidates:
			wait += (end_time - cand[0]) * (-cand[1])
			heappush(ads, [end_time, cand[1]])
	return wait


if __name__ == '__main__':
	print(solution([
		[1,3], [3,2], [5,4]
	]))
	print(solution([
		[0,3], [5,4]
	]))
	print(solution([
		[0,1], [0,2], [6,3], [8,4]
	]))
	print(solution([
		[5, 2], [2,2], [6,3], [9, 2]
	]))