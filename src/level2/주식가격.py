from collections import deque

def solution(prices):
    answer = []
    for idx, price in enumerate(prices):
        sec = 0
        for i in range(idx + 1, len(prices)):
            if price > prices[i]:
                sec += 1
                break
            sec += 1
        answer.append(sec)

    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))