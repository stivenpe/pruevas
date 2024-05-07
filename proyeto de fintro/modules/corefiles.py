import json
import os


MY_PRODUTOS =  "data/"

def Newfile(*param):
    with open(MY_PRODUTOS,"w") as wf:
        json.dump(param[0],wf,indent=4)
        
def addData(*param):
    data =list(param)
    with open(MY_PRODUTOS,"r+") as rwf :
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})
    
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4 )
        
def readfile():
    with open(MY_PRODUTOS,"r") as rf:
        return json.load(rf)                
            
def checkfile(*param):
    data = list(param)
    if(os.path.isfile(MY_PRODUTOS)):
        if(len(param)):
            data[0].update(readfile())        
    else:
        if(len(param)):
            Newfile(data[0]) 