#!/bin/usr/python

from time import sleep
import os
import sys
from Modules.core import *

menu = '''
\033[1;34m[\033[1;32m1\033[1;34m]\033[0;33m Doge Click Bot
\033[1;34m[\033[1;32m2\033[1;34m]\033[0;33m LTC Click Bot
\033[1;34m[\033[1;32m3\033[1;34m]\033[0;33m BCH Click Bot


\033[1;34m[\033[1;32m0\033[1;34m]\033[0;33m Exit
'''

def main():
    banner()
    sleep(1)
    print ('\033[1;96mPilih Dulu Yang Ingin Anda Tuyul')
    print (menu)
    pil = input('\033[1;91mCmbah\033[1;0m >>\033[1;92m ')
    if pil == '1' or pil == '01':
       doge()
    elif pil == '2' or pil == '02':
       ltc()
    elif pil == '3' or pil == '03':
       bch()
    elif pil == '0' or pil == '00':
       sys.exit()

    else:
       print ('\033[1;91mERROR : Wrong Input !')
       sleep(2)
       restart()

if __name__ == "__main__":
       main()
