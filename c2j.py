import os
import sys
import time

import csv
import json

from csvfile import CSVFile


class C2J:
    def __init__(self, csvfile = ''):
        self.csvfile = {"file_details": []}
        if isinstance(csvfile, CSVFile):
            self.convert(csvfile)
    
    def __add__(self, obj):
        concat = C2J()
        concat.csvfile['file_details'] = self.csvfile['file_details'] + obj.csvfile['file_details']
        return concat


    
    def convert(self, csvfile):
        if not isinstance(csvfile, CSVFile):
            raise TypeError(f"{csvfile} is not of type CSVFile")
        csvfile = csvfile.__dict__
        del csvfile['file_path']
        self.csvfile['file_details'] = [csvfile]


    
    def dump(self, filename):
        print('Formatting JSON string (this may take time)...')
        json_string = json.dumps(self.csvfile, indent = 2)
        json_string = json_string.split('\n')
        json_string_mod = ""
        brace_count = -1
        for i in range(len(json_string)):
            line = json_string[i]
            if '[' in line:
                json_string_mod += line
                if '[' in json_string[i + 1]:
                    json_string_mod += '\n'
                brace_count += line.count('[')
                continue
            elif ']' in line:
                brace_count -= line.count(']')
                json_string_mod = json_string_mod[:-1] + line.strip()
                json_string_mod += '\n'
                continue
            if brace_count == 0:
                json_string_mod += line
                json_string_mod += '\n'
            else:
                line = line.strip()
                json_string_mod += line + ' '
        print('JSON string has been formatted.')
        with open(filename, 'w') as json_dump_file:
            json_dump_file.write(json_string_mod)
            print(f'JSON data written to {filename}')



