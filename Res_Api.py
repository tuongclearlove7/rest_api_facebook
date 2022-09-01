import json
import requests

Url_Api = requests.get('https://graph.facebook.com/v14.0/me?fields=id%2Cname%2Cemail%2Cbirthday%2Cgender%2Cage_range%2Clink%2Cname_format%2Caccounts&access_token=EAASCDwYEjcUBAGLpNZBawSTWrTojZCTZCdJdLqB4YpCyM73ZAyEFxykkwBIkXrIx6CWuT9PugVUslLGu0w8XxXUfPTTW8bNQJu3cbBPqhrJfKXWN8rIezyKoi9Y3tHGBhffBDS2H9HzmMNxZBvrbOudKLJDSyZBkJkqhJV47MfHn4VAl8XkMRpRHwAa0U7zLGv4CAoRgnOpAZDZD')

Json_data = Url_Api.text

write_json = open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\json_data.txt',mode='w',encoding='utf-8')
W_json = write_json.write(Json_data)
write_json.close()

with open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\json_data.txt',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def Write_Data(data):
    
        for i in data:
                arrData = i +'\n'
                write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\data.txt",mode='a+',encoding="utf-8")
                W_data = write_data.write(arrData)
                write_data.close() 
                print(arrData)

        return arrData

Write_Data(["_________________________________________________________________________\n",
        'id page : '+value['id'],
        'user name: '+value['name'],
        'email : '+value['email'],
])














