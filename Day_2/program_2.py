"""Question-4:
    
Recursively go below a dir and based on filter, dump those files into single file 
(work with only text file)"""

def get_files(path):
    with open('file_names.txt',"wt") as f:
        for item in os.listdir(path):
            item = path+'\\'+item
            if os.path.isdir(item):
                get_files(item)
            elif '.txt' in item:
                f.writelines(item+'\n')
                
get_files(path)

