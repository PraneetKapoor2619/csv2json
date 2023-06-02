import os
import sys
import time

import platform

os_type = platform.system()

if os_type in ('Linux', 'Darwin'):
    if 'clean' not in sys.argv:
        os.system('python3 csv2json.py samples/data1.csv -o samples/out1.json')
        os.system('python3 csv2json.py -d2 samples/ -o samples/jsons')
        os.system('python3 csv2json.py -d2 -c samples/ -o samples/concat.json')
    else:
        os.system('rm samples/*.json')
        os.system('rm samples/jsons/*.json')

if os_type == 'Windows':
    if 'clean' not in sys.argv:
        os.system('python csv2json.py samples\\data1.csv -o samples\\out1.json')
        os.system('python csv2json.py -d2 samples\\ -o samples\\jsons')
        os.system('python csv2json.py -d2 -c samples\\ -o samples\\concat.json')
    else:
        os.system('del samples\\*.json')
        os.system('del samples\\jsons\\*.json')