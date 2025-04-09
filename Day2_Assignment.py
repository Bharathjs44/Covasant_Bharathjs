'''Question-3:
Given a directory, find out the file Name 
having max size recursively 

'''
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



########################

"""Question-4:
    
Recursively go below a dir and based on filter, dump those files into single file 
(work with only text file)"""

def get_files(directory):
    with open('file_names.txt',"wt") as f:
        for item in os.listdir(directory):
            item = directory+'\\'+item
            if os.path.isdir(item):
                get_files(item)
            elif '.txt' in item:
                f.writelines(item+'\n')
                
get_files(directory)

