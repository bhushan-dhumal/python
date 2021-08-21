import sys
from datetime import datetime
import os

file_name= "_chat.txt"

today = datetime.today().strftime('%d/%m/%y')

d = {}

script_directory = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_directory, file_name)

try:
    f = open(data_file,encoding="utf8")
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))
    sys.exit()

with f:
    lines = f.readlines();
    for line in lines:
        if line[1:9] == today :
            name = line.split("]")[1].split(":")[0]
            if name in d :
                d[name]+=1
            else:
                d[name] = 1
                
print(dict(sorted(d.items(), key=lambda item: item[1], reverse = True)))

## Try to delete the file ##
try:
    os.remove(data_file)
except OSError as e:  ## if failed, report it back to the user ##
    print ("Error: %s - %s." % (e.filename, e.strerror))


