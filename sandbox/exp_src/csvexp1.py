#line 96 "csv2json.web" 
import os
import sys
import csv

os.system('clear')
#line 139 "csv2json.web" 
import pathlib

path = pathlib.Path(__file__).parent.resolve()
print(f"Current path: {path}")

#line 111 "csv2json.web" 
with open('./exp_data/data1.csv', 'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ';')
    print(csvdata)

#line 121 "csv2json.web" 
with open('./exp_data/data1.csv', 'r') as csvfile:
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(csvfile.readline())
    print(f"Delimiter used is {dialect.delimiter}")
    csvfile.seek(0)
    csvdata = csv.reader(csvfile, delimiter = dialect.delimiter)
    for datarow in csvdata:
        print(datarow)

#line 151 "csv2json.web" 
print()
with open('./exp_data/data2.csv', 'r') as csvfile:
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(csvfile.readline())
    print(f"First line: {csvfile.readline()}")
    print(f"Delimiter used is {dialect.delimiter}")
    csvfile.seek(0)
    csvdata = csv.reader(csvfile, delimiter = dialect.delimiter)
    for datarow in csvdata:
        print(datarow)

































































