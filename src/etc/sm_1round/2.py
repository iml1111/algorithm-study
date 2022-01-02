def get_max_pay(times, total_time, n):
    if total_time == 0 or n == 0:
        return 0
    if times[n-1] > total_time:
        return get_max_pay(times, total_time, n-1)
    else:
        return max(
            times[n-1] + get_max_pay(times, total_time - times[n-1], n-1),
            get_max_pay(times, total_time, n - 1)
        )

def solution(pc_num, total_time, reservs):
    answer = []
    users = [[] for i in range(pc_num + 1)]

    for pc_i, time in reservs:
        users[pc_i].append(time)
    for idx in range(1, len(users)):
        cur_pay = get_max_pay(users[idx], total_time, len(users[idx]))
        answer.append((idx, cur_pay * 1000))
    return answer


if __name__ == '__main__':
    print(solution(
        2, 4,
        [
            [1,10],
            [1,5],
            [1,7],

            [2,1],
            [2,3],
            [2, 7],
            [2, 10],
        ]
    ))