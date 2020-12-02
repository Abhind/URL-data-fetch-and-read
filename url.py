#!/usr/bin/env python
import re
import mimetypes
import os
import urllib.request
import shutil
traversal = ["https://www.python.org","https://www.tutorialspoint.com/index.htm"]
i = 1
for line1 in traversal:
    #Created by Abhind( abhinda1996@gmail.com)
    with urllib.request.urlopen(line1) as response, open('%s.txt' %i, 'w') as out_file:
        i +=1
        data = response.read() # a `bytes` object
        data1 = str(data)
        out_file.write(data1)
       
        

   
    
