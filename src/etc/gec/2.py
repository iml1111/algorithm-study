def solution(n):
    if n in (0, 1):
        return str(n)

    if n > 1:
        fibo = [0, 1]
        cur = 2
        answer = fibo[cur-2] + fibo[cur-1]
        while cur < n:
            fibo.append(answer)
            cur = cur + 1
            answer = fibo[cur - 2] + fibo[cur - 1]
        return str(answer)
    else:
        fibo = [1, 0]
        cur = 2
        n = (n - 1) * (-1)
        answer = fibo[cur-2] - fibo[cur-1]
        while cur < n:
            fibo.append(answer)
            cur = cur + 1
            answer = fibo[cur - 2] - fibo[cur - 1]
        return str(answer)


if __name__ == '__main__':
    print(solution(1))
    print(solution(-1))
    print(solution(-4))
    print(solution(3))