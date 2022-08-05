"""https://www.acmicpc.net/problem/1034"""
import sys


def solution(n, m, arr, num):
    all = set([i for i in range(n)])



if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(input())[:-1])))
    num = int(input())
    solution(n, m, arr, num)
