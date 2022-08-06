"""https://www.acmicpc.net/problem/1034"""
import sys
from collections import Counter

def solution(n, m, arr, k):
    arr_cnts = Counter(arr).most_common()

    for row, cnt in arr_cnts:
        zero_cnt = row.count('0')
        if zero_cnt <= k and zero_cnt % 2 == k % 2:
            print(cnt)
            return
    print(0)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(input())
    num = int(input())
    solution(n, m, arr, num)
