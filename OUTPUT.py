# Вывод данных закрытой речи в файл


def record(Fin) :
    k = 0
    output = open('result16.txt', 'w')
    for i in Fin:
        output.write('0x ' + i + '\n')
        k = k + 1
    output.close()
