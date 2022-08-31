import json
import requests

with open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\json\\json_file_test.json',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def Write_Data(data):
        for i in data:
                arrData = i +'\n'
                write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\text data\\data_test.txt",mode='a+',encoding="utf-8")
                W_data = write_data.write(arrData)
                write_data.close() 
                print(arrData)

        return arrData

Write_Data(["_________________________________________________________________________",
        'id page : '+value['id'],
        'name page: '+value['name'],
        'about page : '+value['about'],
        'token : '+value['access_token'],
        'feed id : ' +value['feed']['data'][0]['id'],
        'newfeed status 1 : '+value['feed']['data'][0]['story'],
        'feed created time 1 : '+value['feed']['data'][0]['created_time'],
        'feed id : '+value['feed']['data'][1]['id'],
        'newfeed status 2 : '+value['feed']['data'][1]['story'],
        'feed created time 2 : '+value['feed']['data'][1]['created_time'],
        "id groups : "+value['groups']['data'][0]['id'],
        "name groups : "+ value['groups']['data'][0]['name']
])

     
Write_Data([
        str("before feed : "+value['feed']['paging']['cursors']['before']),
        str("after feed : "+value['feed']['paging']['cursors']['after'])
])       



















        