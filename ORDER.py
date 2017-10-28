# Меняем байты местами

def replace_bytes(str):
    str_buf = ''
    i = 0
    a = len(str) // 4
    b = len(str) // 2
    while i < len(str):
        if (i % b == 0):
            str_buf = str_buf + str[i + a:i + b] + str[i: i + a]
        i = i + 1
    return str_buf


def change_order(array) :
    i = 0
    while i < len(array):
        array[i] = replace_bytes(array[i])
        i = i + 1
    return array