'''
Created on 05/12/2017

@author: 

XXX: https://code.google.com/codejam/contest/975485/dashboard#s=p2
'''

import logging
import sys
from collections import Counter
from functools import reduce
from operator import xor

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def cacandy_core(dulces):
    res_xor = reduce(xor, dulces, 0)
    if(res_xor):
        return 0
    total = sum(dulces) - min(dulces)
    return total

def cacandy_main():
    num_cacasos = int(sys.stdin.readline().strip())
    logger_cagada.debug("cacasos {}".format(num_cacasos))
    for num_cacaso in range(num_cacasos):
        num_dulces = int(sys.stdin.readline().strip())
        logger_cagada.debug("num dulc {}".format(num_dulces))
        dulces = list(map(int, sys.stdin.readline().strip().split(" ")))
#        logger_cagada.debug("dulc {}".format(dulces))
        caca = cacandy_core(dulces)
        print("Case #{}: {}".format(num_cacaso + 1, caca if caca else "NO"))
        
if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        cacandy_main()
