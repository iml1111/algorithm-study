from collections import defaultdict

def solution(lottery):
    check_dict = defaultdict(int)
    num_dict = defaultdict(int)

    for user, result in lottery:
        if check_dict[user] == 0:
            num_dict[user] += 1

        if result == 1:
            check_dict[user] = 1

    user_len = 0
    num_sum = 0
    for user, num in num_dict.items():
        if check_dict[user] == 1:
            num_sum += num
            user_len += 1

    if user_len == 0:
        return 0
    return num_sum // user_len

if __name__ == '__main__':
    print(solution([[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]]))