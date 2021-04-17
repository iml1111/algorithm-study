import re

def StringChallenge(strParam):
    encoder = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    decoder = {
        **{str_i: idx for idx, str_i in enumerate(encoder)},
        "plus": "+", "minus": "-"
    }
    operator = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }
    strParam = re.findall("|".join(decoder.keys()), strParam)
    decodedParam = [decoder[str_i] for str_i in strParam]

    result, i = 0, 0
    while isinstance(decodedParam[i], int):
        result = 10 * result + decodedParam[i]
        i += 1
    op, operand = None, 0
    for param in decodedParam[i:]:
        if param in ['+', '-']:
            if op:
                result = op(result, operand)
                operand = 0
            op = operator[param]
        else:
            operand = 10 * operand + param
    result = str(op(result, operand))

    if not result.startswith('-'):
        return "".join([encoder[int(i)] for i in result])
    else:
        return "negative" + "".join([encoder[int(i)] for i in result[1:]])

# keep this function call here
print(StringChallenge("oneminusoneone"))