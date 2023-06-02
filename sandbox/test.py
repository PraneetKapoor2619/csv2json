import os
import sys
import time

import csv
from csvfile import CSVFile
from c2j import C2J

os.system('clear')
obj1 = CSVFile('./exp_data/data1.csv')
obj2 = CSVFile('./exp_data/data2.csv')
obj1.loadf()
obj2.loadf()

obj1 = C2J(obj1)
#obj1.dump('./exp_data/j1.json')

obj2 = C2J(obj2)
#obj2.dump('./exp_data/j2.json')

obj3 = obj1 + obj2 + obj2 + obj1
obj3.dump('./exp_data/concat.json')
