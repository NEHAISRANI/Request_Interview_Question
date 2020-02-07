import requests
import json
from pprint import pprint
url="https://honored-dirigible.glitch.me/session"
response=requests.get(url)
data=response.json()
# pprint(data)
def studentData(data1):
    for index in data1:
        fileName=(index["emailid"])
        # print(fileName)
        file=('/home/sonam/Desktop/request_interview/' +  (fileName)+".json")
        with open(file,"w")as fileData:
            json.dump(index,fileData)
studentData(data)


