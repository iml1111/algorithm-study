import re

def string_challenge(str_param):
    encoder = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    decoder = {
        **{str_i: idx for idx, str_i in enumerate(encoder)},
        "plus": "+", "minus": "-"
    }
    operator = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }
    str_param = re.findall("|".join(decoder.keys()), str_param)
    decoded_param = [decoder[str_i] for str_i in str_param]

    result, i = 0, 0
    while isinstance(decoded_param[i], int):
        result = 10 * result + decoded_param[i]
        i += 1
    op, operand = None, 0
    for param in decoded_param[i:]:
        if param in ('+', '-'):
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
print(string_challenge("oneminusoneone")) # 1 - 11
print(string_challenge("threeminusfiveplusonetwo")) # 3 - 5 + 12
print(string_challenge("threeminusfiveplusonefour")) # 3 - 5 + 14
print(string_challenge("zerominuszero"))
print(string_challenge("zeropluszero"))
print(string_challenge("minuszeroplusone"))
print(string_challenge("minuszerominusone"))