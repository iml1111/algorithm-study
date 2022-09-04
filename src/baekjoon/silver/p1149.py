"""https://www.acmicpc.net/problem/1149"""
import sys

def solution(n, arr):
    darr = [[0, 0, 0]]
    for i in range(n):
        darr.append([
            min(darr[i][1], darr[i][2]) + arr[i][0],
            min(darr[i][0], darr[i][2]) + arr[i][1],
            min(darr[i][0], darr[i][1]) + arr[i][2]
        ])
    print(min(darr[-1]))


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(n, arr)
