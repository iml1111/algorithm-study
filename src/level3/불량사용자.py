import re
from itertools import product

def solution(user_id, banned_id):
    patterns = [re.compile("^%s$" % i.replace("*", ".")) for i in banned_id]
    matched = [[] for _ in range(len(patterns))]
    for u_idx in range(len(user_id)):
        for p_idx in range(len(patterns)):
            if patterns[p_idx].match(user_id[u_idx]):
                matched[p_idx].append(u_idx)
    
    print(matched)
    producted = product(*matched)
    print(*producted)
    return


if __name__ == '__main__':
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "abc1**"]
    ))
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["*rodo", "*rodo", "******"]
    ))
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"]
    ))