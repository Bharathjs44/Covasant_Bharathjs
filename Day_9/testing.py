import requests

BASE_PATH = " http://127.0.0.1:8000"

def path_params():
	url = f"{BASE_PATH}/helloj/srinu/json"
	res = requests.get(url)
	print(res.json())    
       
         
           
def post():
	url = f"{BASE_PATH}/helloj"
	json_data={"name":"bharathc"}
	params = {"format":"json"}
	res = requests.post(url, json=json_data, params = params )
	print(res.json())



if __name__ == "__main__":
	path_params()
	post()