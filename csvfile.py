import os
import sys
import time

import csv
import ntpath
import platform

class CSVFile:
    def __init__(self, filename):
        self.file_name = None
        self.file_path = None
        self.file_delimiter = None
        self.file_schema = None
        self.file_content = None
        self.set_filename(filename)

    def is_csvfile_valid(self, filename):
        try:
            fp = open(filename, 'r')
        except Exception:
            raise Exception(f"{filename} not found.")

        lines = fp.readlines()
        fp.close()
        if not lines:
            raise Exception(f"{filename} is empty.")

        delimiter = self.guess_delimiter(lines)

        return delimiter

    
    def set_filename(self, filename):
        self.file_delimiter = self.is_csvfile_valid(filename)
        if self.file_delimiter:
            self.file_name = ntpath.basename(filename)
            self.file_name = self.file_name[:self.file_name.rfind('.')]
            self.file_path = ntpath.realpath(filename)
            os_type = platform.system()
            if os_type == 'Linux' or os_type == 'Darwin':
                self.file_path = self.file_path.replace('\\', '/')

    
    def guess_delimiter(self, lines):
        N = 0
        if len(lines) < 50:
            N = len(lines)
        else:
            N = 50

        char_set = set(''.join(lines[:N]))
        char_set.remove('\n')
        char_dict = {key: 0 for key in char_set if not key.isalnum() and key != ' '}
        merr_no_cols = char_dict.copy()
        merr_width_cols = char_dict.copy()

        for key in merr_no_cols.keys():
            cols = 0
            for line in lines:
                cols += len(line.split(key))
            cols /= N
            merr_no_cols[key] = cols

        for key, mean_cols_no in merr_no_cols.items():
            error = 0
            for line in lines:
                error = abs(len(line.split(key)) - (mean_cols_no))
            error /= N
            merr_no_cols[key] = error

        for key in merr_width_cols.keys():
            width = 0
            for line in lines:
                width += len(line.split(key)[0])
            width /= N
            merr_width_cols[key] = width

        for key, mean_col_width in merr_width_cols.items():
            error1 = 0
            for line in lines:
                i = len(line.split(key))
                error1 = abs(len(line.split(key)[0]) - (mean_col_width))
                error2 = abs(len(line.split(key)[i // 2]) - (mean_col_width))
            error1 /= N
            error2 /= N
            merr_width_cols[key] = (error1 + error2)/2

        for char in char_dict.keys():
            char_dict[char] = merr_no_cols[char] + merr_width_cols[char]

        sorted_list = sorted(char_dict.items(), key = lambda item: (item[1], item[0]))
        delimiter = sorted_list[0][0]
        #print(f"Delimiter guessed to be {delimiter}")

        return delimiter


    def loadf(self):
        with open(self.file_path, 'r') as csvfile:
            csvdata = csv.reader(csvfile, delimiter = self.file_delimiter)
            csvdata = list(csvdata)
            self.file_schema = csvdata[0]
            self.file_content = csvdata[1:]

    
    def dumpf(self, filename = '', N = None):
        if filename == '':
            filename = self.file_path
        if N is None:
            N = len(self.file_content)
        with open(filename, 'w') as csvfile:
            writerobj = csv.writer(csvfile, delimiter = self.file_delimiter)
            writerobj.writerow(self.file_schema)
            writerobj.writerows(self.file_content[:N])





