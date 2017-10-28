# Вводим модули, в которых расположены составляющие программы

import READ
import DECOMP
import TRANSFORM
import CHANGEFORMAT
import ORDER
import FINAL
import OUTPUT

OUTPUT.record(FINAL.make_kadr(ORDER.change_order(CHANGEFORMAT.structuring(TRANSFORM.reduct(DECOMP.decompose_to_list(READ.read_from_file()))))))





