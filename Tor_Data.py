#!/usr/bin/env python
import re
import mimetypes
import os
# all declarations
path = 'C:\Abhind Work\Script\Test'
out_val = "('text/plain', None)"
in_val = "test"
in_val1 = "test"
temp_list1 = []
traversal = []
keyword = []
# funcrion defination
def match(temp_list1):
    f3 = open("keyword.txt", "r")
    for key in f3:
        keyword.append(key.rstrip())
        print(key)
    f3.close()
    with open("output.txt", "a") as f1:
     for line in temp_list1:
         #print(line)
         f1.write("*******************************************************************************************************************************************")
         f1.write("\n")
         f1.write("File Path:")
         f1.write("\n")
         f1.write(line)
         f1.write("\n")
         f1.write("********************************************************************************************************************************************")
         f1.write("\n")
         f2 = open(line, "r")
         for line1 in f2:
             for line2 in keyword:
                 if re.findall(line2, line1):
                         f1.write(line2)
                         #f1.write(line1)
                         f1.write("\n")
                 else:
                         f1.write(" ")
    return

#File Traversal in a directory
files = []
# r=root, d=directories, f = files
print(os.listdir())
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
            #print(file)

#print(files)
for f1 in files:
        #Phone = open(f, "r")
        in_val = mimetypes.guess_type(f1, strict=True)
        #print(in_val)
        #Created by Abhind( abhinda1996@gmail.com)
        # As .txt file returns 'text/plain, None' and log file returns None, None; i am excluding the text file from processing and only considering the log files
        if not'gzip' in in_val:
            #print(in_val)
            traversal.append(f1)
#print(traversal)
match(traversal)
