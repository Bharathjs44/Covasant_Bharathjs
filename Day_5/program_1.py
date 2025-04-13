#############@@@@ Day_5 @@@@###############
########concurrent programming ############

import requests
import os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time

   
def fetch_process_links(url):
    print(f"Connecting to {url}.....")
    time.sleep(2)
    
    try:
        resp = requests.get(url)
        if resp.ok:            #resp.raise_for_status()
            s = BeautifulSoup( resp.text,'html.parser')
            a_tags = set()
            for a_tag in s.find_all('a',href = True):
                a_tags.add(a_tag['href'])
            print(f" Extracted {len(a_tags)} links.")

            with ThreadPoolExecutor(max_workers = 10) as executor:
                executor.map(download, a_tags)
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    
    except requests.RequestException as error:
        print(f" An error occured :{error}")
           
           
def download(url):
    print(f"Initiating download from: {url} ")
    time.sleep(2)
    print(f" Download complete for: {url}")
    

if __name__=="__main__":
    st=time.time()
    url = r"https://www.google.co.in"
    fetch_process_links(url)
    et = time.time()
    total_time = et-st
    print(f"\n Total Execution Time:{total_time}")
    
    
    

#output:  

'''C:\Users\Bharath\Desktop\Covasant_Bharathjs\Day_5>python program_1.py
Connecting to https://www.google.co.in.....
 Extracted 27 links.
Initiating download from: http://www.google.co.in/history/optout?hl=en
Initiating download from: https://www.youtube.com/?tab=w1
Initiating download from: https://www.google.co.in/setprefdomain?prefdom=US&sig=K_2JenrY5M3kF5EFhcBlzOi5yGqa0%3D
Download complete for: https://www.google.co.in/setprefs?sig=0_eU9DjSld7OBwHSGVnWvCdZDyvu8%3D&hl=gu&source=homepage&sa=X&ved=0ahUKEwi389a1rdSMAxWPIrkGHUfnIbIQ2ZgBCAs
Download complete for: https://www.google.co.in/setprefs?sig=0_eU9DjSld7OBwHSGVnWvCdZDyvu8%3D&hl=te&source=homepage&sa=X&ved=0ahUKEwi389a1rdSMAxWPIrkGHUfnIbIQ2ZgBCAg

Total Execution Time:9.266940832138062'''

