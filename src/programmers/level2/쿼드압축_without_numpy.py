def list_cut(arr, i, j, n2):
    map = [0, n2, n2 * 2]
    result = []
    for i in range(map[i], map[i+1]):
        result.append(arr[i][map[j]:map[j+1]])
    return result

def compress(arr, n):
    arr_sum = sum([sum(i) for i in arr])
    nn, n2= n * n, n // 2
    if arr_sum == nn:
        return 0, 1
    elif arr_sum == 0:
        return 1, 0
    else:
        zero, one = 0, 0
        for i in range(2):
            for j in range(2):
                z_, o_ = compress(list_cut(arr, i, j, n2), n2)
                zero += z_
                one += o_
        return zero, one

def solution(arr):
    zero, one = compress(arr, len(arr))
    return [zero, one]


if __name__ == '__main__':
    result = solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
    print(result)