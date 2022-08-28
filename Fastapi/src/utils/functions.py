
def calculate(a, b, cal_type):
    if param.cal_type == '더하기':
        value = param.a + param.b
    elif param.cal_type == '빼기':
        value = param.a - param.b
    elif param.cal_type == '곱하기':
        value = param.a * param.b
    elif param.cal_type == '나누기':
        value = param.a / param.b
    else:
        return {
            'error': 'cal_type must be one of "더하기", "빼기", "곱하기, or "나누기".'}
    return {'result': value}

# value error를 일으켜 HTTP status code를 400번대로 변경해야함 