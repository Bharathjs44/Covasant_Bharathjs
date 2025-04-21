from program_2 import Files
from datetime import datetime ,date

fs = Files(r"C:\Users\Bharath\Desktop\Handson")
print(fs.get_MaxSize_file(3))  
print(fs.get_Latest_Files(date(2025,4,11))) 

