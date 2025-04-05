'''Question-3:
Given a directory, find out the file Name 
having max size recursively 

Question-4:
Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)'''
#######################Day2-Assignment###############################
# program-3

import os

directory=(r"C:\Users\Bharath\Desktop\Covasant_Bharathjs")

max_size=-1
   
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path=os.path.join(root,file)
        size =os.path.getsize(file_path)
        if size > max_size:
            max_size=size
            largest_file = file_path
  
print(f"File Name:{largest_file}")
print(f"size of the file :{max_size} bytes")
  

