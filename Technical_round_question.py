import requests
#this script will give output in console>>>>

#same function i used during technical round to explain the pseudocode as recursion 
def my_function(space, json_data):
    for value in json_data:
        print(space+value['name'])
        my_function(space+" "*2, value['child'])

url="https://raw.githubusercontent.com/Vibencode-Solutions/mock-api/main/api.json"

response = requests.get(url)

if response.status_code==200:
    print("*********succes message**********")
    print("*************data***************")
    data=response.json()
    my_function("", data)#function i used during the technical round   
else:
    print("error message")
    print(response.status_code)

