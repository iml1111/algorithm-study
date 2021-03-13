
def is_two(arr):
    cnt = 0
    for i in arr:
        for _ in i:
            cnt += 1
    return cnt == 2

def get_max(left, right):
    left_max = max([max(i) for i in left])
    if is_two(right):
        right_max = max([max(i) for i in right])
    else:
        n = len(right)
        m = len(right[0])
        quarters = []
        if 1 < m:
            quarters.append(get_max([i[:m // 2] for i in right], [i[m // 2:] for i in right]))
            quarters.append(get_max([i[m // 2:] for i in right], [i[:m // 2] for i in right]))
        if 1 < n:
            quarters.append(get_max([i for i in right[:n//2]], [i for i in right[n//2:]]))
            quarters.append(get_max([i for i in right[n//2:]], [i for i in right[:n//2]]))
        right_max = max(quarters)
    return left_max + right_max


def solution(arr):
    n = len(arr)
    return max(
        get_max([i[:n // 2] for i in arr], [i[n // 2:] for i in arr]),
        get_max([i[n // 2:] for i in arr], [i[:n // 2] for i in arr]),
        get_max([i for i in arr[:n//2]], [i for i in arr[n//2:]]),
        get_max([i for i in arr[n//2:]], [i for i in arr[:n//2]])
    )


if __name__ == '__main__':
    print(solution(
        [
            [1,3,4,5],
            [6,2,9,9],
            [4,3,10,5],
            [5,2,8,6]
        ]
    ))