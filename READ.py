#Выбираем из начальной последовательности 0 и 1 и записываем их в строку

def separate_01(str) :
    str_res = ''
    for symbol in str :
        if symbol in ('0', '1') :
            str_res = str_res + symbol
    return str_res

def read_from_file() :
    input = open('gamma_450k.txt')
    str_start = input.read()
    str_res = separate_01(str_start)
    return str_res