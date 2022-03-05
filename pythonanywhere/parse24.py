import sys
from datetime import datetime,timedelta
import os

file_name= "_chat.txt"
d = {}
nowTime=datetime.now()
past = nowTime - timedelta(days=1)
print("Counts are from {} to {}".format(past.strftime("%d/%m/%y, %I:%M:%S %p"),nowTime.strftime("%d/%m/%y, %I:%M:%S %p")))
script_directory = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_directory, file_name)

try:
    f = open(data_file,encoding="utf8")
    with f:
        lines = f.readlines();
        for line in lines:
            try:
                if len(line.split("[")) > 1 :
                    time = line.split("[")[1].split("]")[0] 
            except IndexError:
                 print("Index Error for time in "+line)
            if len(time) <=0 : continue
            datetime_object = datetime.strptime(time,"%d/%m/%y, %I:%M:%S %p")
            if datetime_object > past :
                try:
                    if len(line.split("]")) > 1 :
                        name = line.split("]")[1].split(":")[0]
                except IndexError:
                    print("Index Error for "+line)
                    
                if len(name) <= 0:
                    continue
                if name[1] == '\u200e':
                    continue
                if name in d :
                    d[name]+=1
                else:
                    d[name] = 1
                
    print(dict(sorted(d.items(), key=lambda item: item[1], reverse = True)))

    ## Try to delete the file ##
    os.remove(data_file)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))
    sys.exit()



