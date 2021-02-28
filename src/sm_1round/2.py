def solution(pc_num, total_time, reservs):
    answer = []
    users = [[] for i in range(pc_num + 1)]

    for pc_i, time in reservs:
        users[pc_i].append(time)
    for idx in range(1, len(users)):
        users[idx].sort()
        cur_time, cur_pay, i = total_time, 0, 0
        while cur_time > 0 and users[idx][i] <= cur_time:
            cur_pay += users[idx][i]
            cur_time -= users[idx][i]
        answer.append((idx, cur_pay * 1000))
    return answer


if __name__ == '__main__':
    print(solution(
        2, 4,
        [
            [1,10],
            [1,5],
            [1,7],
            [2,10],
            [2,1],
            [2,3],
            [2,7]
        ]
    ))