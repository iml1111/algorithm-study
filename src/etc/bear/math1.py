def is_int(param: str):
    if param[0] == '-':
        return param[1:].isdigit()
    else:
        return param.isdigit()

def MathChallenge(strParam):
    strParam = strParam.split()
    stack = []
    for str_i in strParam:
        if is_int(str_i):
            stack.append(str_i)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if str_i == "+":
                stack.append(str(a + b))
            elif str_i == "-":
                stack.append(str(a - b))
            elif str_i == "*":
                stack.append(str(a * b))
            else:
                stack.append(str(a // b))

    # code goes here
    return int(stack[0])

# keep this function call here
print(MathChallenge("3 3 + 2 /"))