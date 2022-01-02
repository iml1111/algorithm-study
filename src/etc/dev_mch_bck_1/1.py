def zero_cnt(array):
    cnt = 0
    for i in array:
        if i == 0:
            cnt += 1
    return cnt

def solution(lottos, win_nums):
    optional_cnt = zero_cnt(lottos)
    lottos = set(lottos)
    win_nums = set(win_nums)
    required_cnt = len(lottos & win_nums)
    rank = [6,6,5,4,3,2,1]
    return [rank[required_cnt + optional_cnt], rank[required_cnt]]

if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))