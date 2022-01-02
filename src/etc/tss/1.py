from collections import defaultdict

def solution(name_list):
    name_dict = defaultdict(int)
    answer = []
    for name in name_list:
        alpha = chr(ord('A') + name_dict[name])
        name_dict[name] += 1
        answer.append(name + alpha)
    return answer

if __name__ == '__main__':
    print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))