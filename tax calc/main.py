from dict import *


def transcribe(number):
    parts = ['000', '000', '000', '000']  # Классы записаны в обратном порядке сотни - тысячи - миллионы
    result_text = ''
    for i in range(0, len(number), 3):
        clas = 0
        if i == 0:
            clas = number[-3:]
        else:
            clas = number[(-3 - i):(-i)]
        clas = '0' * (3 - len(str(clas))) + str(clas)
        parts[i // 3] = clas

    parts.reverse()

    count = 4
    for part in parts:
        if part == '000':
            count -= 1
            continue
        if count == 4:
            if part[1] == '1':
                text = hundreds[part[0]] + singles[part[1:]] + billions['0']
            else:
                text = hundreds[part[0]] + decades[part[1]] + billions[part[2]]
        elif count == 3:
            if part[1] == '1':
                text = hundreds[part[0]] + singles[part[1:]] + millions['0']
            else:
                text = hundreds[part[0]] + decades[part[1]] + millions[part[2]]
        elif count == 2:
            if part[1] == '1':
                text = hundreds[part[0]] + singles[part[1:]] + thousands['0']
            else:
                text = hundreds[part[0]] + decades[part[1]] + thousands[part[2]]
        elif count == 1:
            if part[1] == '1':
                text = hundreds[part[0]] + singles[part[1:]]
            else:
                text = hundreds[part[0]] + decades[part[1]] + singles[part[2]]
        result_text = result_text + text
        count -= 1

    if result_text == '':
        result_text = 'ноль'

    print(result_text)
    return result_text
