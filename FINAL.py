# Выделяем кадры закрытой речи и отбарсываем все остальное

def make_speech(kadr):
    speech = ''
    i = 0
    while i < len(kadr):
        if (i % 24 == 0):
            speech = speech + kadr[i: i + 6]
        i = i + 1

    i = 954
    k = 0
    while i < 2857:
        if (k % 24 == 0):
            speech = speech + kadr[i: i + 6]
        k = k + 1
        i = i + 1
    speech = speech[2::3]
    return speech



def make_kadr(array):
    kadr = ''
    i = 0
    final_array = []
    while i < len(array):
        if (i > 0) & (i % 160 == 0):
            final_array.append(make_speech(kadr))
            kadr = ''
        kadr = kadr + array[i]
        i = i + 1
    return final_array

