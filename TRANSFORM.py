#В строках по 128 бит удаляем каждый второй символ и оставшиеся символы инвертируем

def invert(str):
    str_buf = ''
    for i in str:
        if i == '0':
            str_buf = str_buf + '1'
        else:
            str_buf = str_buf + '0'
    return str_buf

def reduct(array) :
    i = 0
    while i < len(array):
        array[i] = array[i][::2]
        array[i] = invert(array[i])
        i = i + 1
    return array
