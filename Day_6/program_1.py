import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

async def download(url):
    print(f"Initiating download from: {url} ")
    await asyncio.sleep(2)
    print(f" Download complete for: {url}")
    
async def fetch_process_links(session, url):
    print(f"Connecting to {url}.....")
    await asyncio.sleep(2)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:        
                bs = BeautifulSoup(await resp.text(),'html.parser')
                a_tags = set()
                for a_tag in bs.find_all('a',href = True):
                    a_tags.add(a_tag['href'])
                print(f" Extracted {len(a_tags)} links.")
                return a_tags

            else:
                print(f"Failed : {resp.status}")
                
    except Exception as e:
        print(f" An error occured :{e}")
    return []
    
async def main(url):
    async with aiohttp.ClientSession() as sess:
        urls = await fetch_process_links(sess, url)
        await asyncio.gather(*(download(link) for link in urls))
        
if __name__=="__main__":
    start =time.time()
    asyncio.run(main(r"https://www.google.co.in"))
    print(f"\n Total Execution Time:{time.time() - start: .2f} seconds")
    


'''#output:
Connecting to https://www.google.co.in.....
Extracted 27 links.
Initiating download from: /preferences?hl=en
Initiating download from: https://www.google.co.in/setprefs?sig=0_mn4Q2O-LLnp1kUtntdKHkqF4hfo%3D&hl=kn&source=homepage&sa=X&ved
Download complete for: https://www.google.co.in/setprefs?sig=0_mn4Q2O-LLnp1kUtntdKHkqF4hfo%3D&hl=hi&source=homepage&sa=X&ved
Total Execution Time: 4.78 seconds'''