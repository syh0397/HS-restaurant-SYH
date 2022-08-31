
def calculate(a, b, cal_type):
    if cal_type == 'addition':
        return a + b
    elif cal_type == 'subtraction':
        return a - b
    elif cal_type == 'multiplication':
        return a * b
    elif cal_type == 'division':
        return a / b
    else:
        raise ValueError('cal_type must be one of "addition", "subtraction", "multiplication, or "division".')

# value error를 일으켜 HTTP status code를 400번대로 변경해야함 