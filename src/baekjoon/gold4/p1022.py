import sys


def solution(r1, c1, r2, c2):
    r = max(abs(r1), (r2))
    c = max(abs(c1), abs(c2))
    n = (max(r, c) * 2) + 1


    arr = [[0 for _ in range(c2 - c1 + 1)]
           for _ in range(r2 - r1 + 1)]
    arr_filled = 0
    max_arr_len = len(arr) * len(arr[0])
    arr_max_num = 0

    flag = 0
    i, j = n - 1, n - 1
    num = n * n
    visited = set()

    r1 += (n - 1) // 2
    r2 += (n - 1) // 2
    c1 += (n - 1) // 2
    c2 += (n - 1) // 2

    while arr_filled < max_arr_len:

        visited.add((i, j))

        if r1 <= i <= r2 and c1 <= j <= c2:
            arr[i - r1][j - c1] = num
            arr_max_num = max(num, arr_max_num)
            arr_filled += 1

        if flag == 0:
            if 0 < j and (i, j-1) not in visited:
                j -= 1
            else:
                flag = 1
                i -= 1

        elif flag == 1:
            if 0 < i and (i-1, j) not in visited:
                i -= 1
            else:
                flag = 2
                j += 1

        elif flag == 2:
            if j < n - 1 and (i, j+1) not in visited:
                j += 1
            else:
                flag = 3
                i += 1

        else:
            if i < n - 1 and (i+1, j) not in visited:
                i += 1
            else:
                flag = 0
                j -= 1

        num -= 1

    for arr_i in arr:
        for i in arr_i:
            print(str(i).rjust(len(str(arr_max_num))), end=" ")
        print()


if __name__ == '__main__':
    input = sys.stdin.readline
    inputs = list(map(int, input().split()))
    solution(*inputs)