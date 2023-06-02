import os
import sys
import time

import ntpath
import pathlib

import re
import csv
import json

from csvfile import CSVFile
from c2j import C2J


def main():
    argvlist = sys.argv[1:]
    depth = False
    concatenate = False
    input_path = ''
    output_path = ''

    for argv in argvlist:
        if '-d' in argv or '--depth' in argv:
            extr = re.findall('[0-9]+', argv)
            depth = int(extr[0])
        elif '-c' in argv or '--concat' in argv:
            concatenate = True
        elif '-o' in argv:
            pass
        else:
            if input_path == '':
                input_path = argv
            else:
                output_path = argv

    if depth is not False or concatenate is not False:
        if depth is False and concatenate is not False:
            depth = 1
        if not os.path.isdir(input_path):
            raise Exception(f'{input_path} is not a directory')
        if concatenate is False:
            if not os.path.isdir(output_path):
                raise Exception(f'{output_path} is not a directory')
    else:
        if not os.path.isfile(input_path):
            raise Exception(f'File {input_path} does not exists')

    input_files = []
    if depth is not False:
        for (dirpath, subdirs, filenames) in os.walk(input_path):
            if depth == 0:
                break
            for filename in filenames:
                if '.csv' in filename:
                    input_files.append(dirpath + os.sep + filename)
            depth -= 1
    else:
        input_files.append(input_path)
    print(input_files)

    csvfile_objs = []
    c2j_objs = []
    for file in input_files:
        csvfile_obj = CSVFile(file)
        csvfile_obj.loadf()
        c2j_obj = C2J(csvfile_obj)
        csvfile_objs.append(csvfile_obj)
        c2j_objs.append(c2j_obj)


    c2j_sum = C2J()
    for i in range(len(csvfile_objs)):
        if len(input_files) == 1:
            c2j_objs[i].dump(output_path)
        elif len(input_files) > 1:
            if concatenate is True:
                c2j_sum += c2j_objs[i]
            elif concatenate is False:
                filename = csvfile_objs[i].file_name + '.json'
                c2j_objs[i].dump(output_path + os.sep + filename)
    if concatenate is True:
        c2j_sum.dump(output_path)




main()

