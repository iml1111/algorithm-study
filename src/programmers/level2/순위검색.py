
def refine_info(infos):
    array = []
    for info in infos:
        item = info.split()
        item[-1] = int(item[-1])
        array.append(item)
    array.sort(key=lambda x: x[-1])

    result = {}
    for lang in ('cpp', 'java', 'python', '-'):
        for pos in ('frontend', 'backend', '-'):
            for career in ('junior', 'senior', '-'):
                for food in ('chicken', 'pizza', '-'):
                    result[f"{lang} and {pos} and {career} and {food}"] = []

    for info in array:
        for lang in (info[0], '-'):
            for pos in (info[1], '-'):
                for career in (info[2], '-'):
                    for food in (info[3], '-'):
                        result[f"{lang} and {pos} and {career} and {food}"].append(int(info[4]))

    return result


def solution(info, query):
    info = refine_info(info)
    answer = []

    for q in query:
        point = int(q[q.rfind(" ") + 1:])
        q = q[:q.rfind(" ")]
        target = info[q]

        l = len(target)
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if point <= target[mid]:
                tmp = mid
                high = mid - 1
            else:
                low = mid + 1
        answer.append(l - tmp)
    return answer


if __name__ == '__main__':
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
        "- and - and - and - 210",
        'cpp and backend and senior and - 50'
    ]

    print(solution(info, query))