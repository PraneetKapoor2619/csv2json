CSV2JSON: A Python Script for Converting CSV Files to JSON
==========================================================

CSV2JSON is a Python script which converts CSV files to their JSON counterparts. Of course, this thing can be
done within a couple of lines of Python, but I wanted the output to be in a specific format. Traditionally, if
you will convert a list object to a JSON object with indentation, you will see that the resulting string has
individual elements occupying whole lines.  
  
```JSON
[
    "a",
    "b",
    "c"
]
```
  
I did not want this. Instead I wanted the list representing a row to be nicely stacked in one single line.  
  
```JSON
["a", "b", "c"]
```

I also wanted to implement an automatic delimiter detector for CSV files. The traditional Sniffer() class
provided with the `csv` module was unable to guess the delimiter had I used something like `~` or `#` as a
delimiter. So, I wrote my own delimiter guessing algorithm.  
  
Essentially csv2json.py is a command line utility. Here is how you can use it:
**NOTE:** For the last two modes of operations presented below, CSV files must end with `.csv` extension else
this program won't catch them during directory traversal.

1. If you wish to convert a single CSV file to a JSON file:  

```bash
    python csv2json.py path/to/file1/file1.csv -o path/to/file2/file2.json
```

2. If you wish to convert all the CSV files present under a directory to their corresponding JSON files in
   some other directory:  
  
```bash
    python csv2json.py -dn path/to/csv/files/ -o path/to/json/files/
```

  Here `-d` (or `--depth`) flag denotes the depth till which the first directory should be searched for CSV files.

3. If you wish to convert all the CSV files present under a directory to their corresponding JSON representations,
   concatenate these, and write them to a single JSON file, then use `-c` or `--concatenate` flag:  
  
```bash
    python csv2json.py -dn -c path/to/csv/files/ -o path/to/json/file/file.json
```
  
You can play with the data given in `samples` directory. I am including a Python script `play.py` which
executes a bunch of commands to give you an idea about how to use this utility:  

```bash
    python play.py
```
  
To clean up after running `play.py`, you can run the same script with `clean` flag:

```bash
    python play.py clean
```

If you want to know the thought-process behind the code, kindly refer to csv2json.web present in `sandbox/`.
This project was basically developed in `sandbox` directory as a literate program. When the code was ready, it
was moved here.

