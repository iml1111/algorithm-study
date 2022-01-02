# -*- coding: utf-8 -*- 
'''
월간 코딩 챌린지 시즌 2
- 두개 뺴서 더하기
'''


def solution(numbers):
    answer = set()
    num_len = len(numbers)
    
    for i in range(num_len):
        for j in range(num_len):
            if i != j:
                answer.add(numbers[i] + numbers[j])
    
    answer = list(answer)
    answer.sort()
    return answer


if __name__ == '__main__':
    numbers = [2,1,3,4,1]
    result = solution(numbers)
    print(result)