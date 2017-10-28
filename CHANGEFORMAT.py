# Удаляем последние 4 байта, а оставшиеся переводим в 16-ричную систему счисления

def make_hex(str) :
    str_buf = ''
    i = 0
    while i < len(str):
        if (i % 4 == 0):
            str_buf = str_buf + hex(int(str[i:i+4],2))
        i = i + 1
    return str_buf


def structuring(array) :
    i = 0
    while i < len(array):
        array[i] = array[i][:32] # Удаляем последние 4 байта
        array[i] = make_hex(array[i])
        i = i + 1
    return array
