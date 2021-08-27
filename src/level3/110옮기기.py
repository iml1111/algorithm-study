def extract(string):
    count, stack = 0, []
    for ch in string:
        if (ch == '0' and 2 <= len(stack)
            and stack[-1] == stack[-2] == '1'):
            del stack[-2:]
            count += 1
        else:
            stack.append(ch)
    return ''.join(stack), count

def solution(s):
    answer = []
    for s_i in s:
        s_i, cnt = extract(s_i)
        zero = s_i.rfind("0")
        if zero == -1:
            answer_i = "110" * cnt + s_i
        else:
            answer_i = s_i[:zero + 1] + "110" * cnt + s_i[zero + 1:]
        answer.append(answer_i)
    return answer
