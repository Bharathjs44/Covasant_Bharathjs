#program-1
 
 #GIVEN TASK
 
#a = Poly(1,2,3)  #an, ...., a0 
#b = Poly(1,0,1,1,2,3)
#c = a+b 
#print(c) #Poly ( 1,0,1, 2,4,6)

'''class Poly:
    def __init__(self, *args):
        self.data =list(args)
        
    def __add__(self, differ):
        i,j =len(self.data),len(differ.data)
        if i < j:
            self.data = [0]*(j-i)+self.data
        else:
            differ.data = [0]*(i-j)+differ.data
        res=[]  
        for i,j in zip(self.data,differ.data):
            res.append(i+j)
        
        return Poly(*res)
    
    def __repr__(self):
        return f"Poly({','.join(map(str,self.data))})"
            
    
if __name__ == '__main__':
    a = Poly(1,2,4,2,3,2)
    b = Poly(1,0,1,2)
    c = a + b
    print(c)
        
        
#output: Poly(1,2,5,2,4,4)    
        
    '''
####################################################################################       
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
        
        
fs = Files(r"C:\Users\Bharath\Desktop\Handson")
   
print(fs.get_MaxSize_file(3)) 
  
print(fs.get_Latest_Files(date(2025,4,11))) 

    
        
    
    
    