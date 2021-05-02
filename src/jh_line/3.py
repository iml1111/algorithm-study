def solution(ads):
	ads.sort(key= lambda x: (x[0], -x[1]))

if __name__ == '__main__':
	print(solution([
		[1,3], [3,2], [5,4]
	]))