
def get_timestep(info):
    time_step = set()
    for idx, (_, step) in enumerate(info):
        info[idx][1] = set(step)
        time_step.update(info[idx][1])
    return sorted(list(time_step))

def solution(info):
    answer = 0
    time_step = get_timestep(info)
    info.sort(key=lambda x: -x[0])
    for cur_step in time_step:
        for score, steps in info:
            if cur_step in steps:
                answer += score
                break
    return answer


if __name__ == '__main__':
    print(solution(
        [
            [1, [1,3,5]],
            [2, [2,4]],
            [3, [1,2]],
            [4, [3]],
        ]
    ))