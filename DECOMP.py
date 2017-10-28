# Раскладываем строку в список строк по 128 бит

def decompose_to_list(str) :
    i = 0
    array = []
    while i < len(str):
        if (i % 129 == 0):
            array.append(str[i: i + 128])
        i = i + 1
    return array
