'''Question-3:
Given a directory, find out the file Name 
having max size recursively 

'''
#######################Day2-Assignment###############################
# program-3

import os
import glob


def get_max_file(path):
    def get_files(path, dic={}):
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                dic[file] = os.path.getsize(file)
            elif os.path.isdir(file):
                get_files(file, dic)
        return dic
    
    files_list = get_files(path)
    mfile = sorted(files_list, key=lambda k: files_list[k])    
    return mfile[-1] 

path=(r"C:\Users\Bharath\Desktop\Covasant_Bharathjs")

print(f"Max_file is :",get_max_file(path))