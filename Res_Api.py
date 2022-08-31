import json
import requests

Url_Api = requests.get('https://graph.facebook.com/v14.0/me?fields=id%2Cname%2Caccess_token%2Cfeed%2Cabout%2Cgroups&access_token=EAASCDwYEjcUBALc4atWu8VI1MvTMg6CL7KUxMvJm7R2dFNG4yho1gzMgVAVWpzX3M3cBKDcu23Gof9VTZB0VrLOHYtBAq8jcuYHciyU2vZBiPmdYfJCaYouh17w7BRHzdArUJpnhGHRIytZCPA3Ixq2qUTsIKPAq8h2gmV8lw8z3ag9XBZAAKFDtK9ZAvrZAnt6ZBml8cNuRAZDZD')

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


Write_Data(["_________________________________________________________________________",
        'id page : '+value['id'],
])















