import glob
import os
import datetime
from datetime import datetime ,date
import time
       
class Files:
    def __init__(self,path):
        self.path = path   
        
    def get_Files(self, path, ed={}):
        files = glob.glob(os.path.join(path, "*"))
        for f in files:
            if os.path.isfile(f):
                ed[f] = os.path.getsize(f)
            elif os.path.isdir(f):
               self.get_Files(f, ed)
        return ed   
        
    def get_MaxSize_file(self, n=1):
        files =self.get_Files(self.path)
        return sorted(files, key = lambda file:files[file])[-n:]
    
    def get_Latest_Files(self,date):
        files = self.get_Files(self.path)
        dt = datetime.combine(date, datetime.min.time())
        sec = int(dt.timestamp())
        return [file for file in self.get_Files(self.path)
            if os.path.getctime(file) > sec]
        
        
#fs = Files(r"C:\Users\Bharath\Desktop\Handson")
#print(fs.get_MaxSize_file(3))         

#output: 
    ['C:\\Users\\Bharath\\Desktop\\Handson\\Day7\\static\\favicon.ico', 
     'C:\\Users\\Bharath\\Desktop\\Handson\\Day3\\Day3.txt', 
     'C:\\Users\\Bharath\\Desktop\\Handson\\Day6\\iris.db']
          
#print(fs.get_Latest_Files(date(2025,4,11))) 

#output:
    ['C:\\Users\\Bharath\\Desktop\\Handson\\Day6\\quick_server.py', 
     'C:\\Users\\Bharath\\Desktop\\Handson\\Day7\\exercise.py',  
     'C:\\Users\\Bharath\\Desktop\\Handson\\Day7\\quick_server.py',]