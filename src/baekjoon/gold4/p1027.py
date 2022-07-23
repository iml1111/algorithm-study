import sys

def get_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solution(buildings):
    max_cnt = 0
    for x1, y1 in enumerate(buildings):
        left, right = x1 - 1, x1 + 1
        left_cnt, right_cnt = 0, 0
        left_slope, right_slope = None, None
        while left >= 0:
            slope = get_slope(x1 + 1, y1, left + 1, buildings[left])
            if left_slope is None or left_slope > slope:
                left_slope = slope
                left_cnt += 1
            left -= 1
        while right < len(buildings):
            slope = get_slope(x1 + 1, y1, right + 1, buildings[right])
            if right_slope is None or right_slope < slope:
                right_slope = slope
                right_cnt += 1
            right += 1
        max_cnt = max(max_cnt, left_cnt + right_cnt)
        #print(x1 + 1, left_cnt, right_cnt)
    print(max_cnt)


if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())
    buildings = list(map(int, input().split()))
    solution(buildings)
    #solution([1, 5, 3, 2, 6, 3, 2, 6, 4, 2, 5, 7, 3, 1, 5])
    #solution([1, 2, 7, 3, 2])
    #solution([1000000000, 999999999, 999999998, 999999997, 999999996, 1, 2, 3, 4, 5])