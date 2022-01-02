from collections import deque

def solution(arr, k):
    order_arr = list(range(1, len(arr) + 1))
    arr_len = len(arr)

    q = deque([(arr, 0)])
    result = float('inf')

    while q:
        cur_arr, cur_cnt = q.popleft()
        if cur_arr == order_arr:
            result = min(result, cur_cnt)
        else:
            for i in range(1, arr_len):
                for j in range(i - k, i):
                    if 0 <= j and cur_arr[j] > cur_arr[i]:
                        temp_arr = cur_arr[:]
                        temp_arr[i], temp_arr[j] = temp_arr[j], temp_arr[i]
                        q.append((temp_arr, cur_cnt + 1))

    return result

if __name__ == '__main__':
    print(solution([4, 5, 2, 3, 1], 2))