import numpy as np
import pandas as pd
import re

file_name='<Your_file_name without extension>'
path='./'+file_name
path_txt=path+'.txt'
path_csv=path+'.csv'
with open(path_txt,'r') as file:
    _data=file.read()
data='Date,Time,Sender,Message\n'.replace(',','<comma>')
for line in _data.split('\n'):
    if re.match('[0-9][0-9]/[0-9][0-9]/[0-9][0-9]',line[:8]):
        line=line.replace(': ','<comma>')
        lined=list(line)
        lined[8]='<comma>'
        lined=''.join(lined)
        data+='\n'+lined
    else:
        data+=line        
#print(data)  
datata=[]
for dt in data.split('\n'):
    k=dt.split('<comma>')
    if len(k)==4:
        datata.append(k)
df=pd.DataFrame(datata[1:],columns=datata[0])
df.dropna()
df.to_csv(path_csv)
print("done")
