import json
import requests

Url_Api = requests.get('https://graph.facebook.com/v14.0/me?fields=id%2Cname%2Cabout%2Caccess_token%2Cgroups%2Cfeed&access_token=EAASCDwYEjcUBAEC1KZBAEjrJ57K0aH02Q7QCUflZAooPpCK64Lpch17BuqZARpWzBACInHrAJhTZBHWP0PeVXGrGR1cpWOLZAI3YiYT2T2Q2IcujI7hset4MyZCfWufBPanZC9fzh2q6E9uQjNkXO2P19WX8dMK4ILvsM6kPjzrpqdHyJBDgmTp0EW08nVURRl67CEfRZC39IAZDZD')

Json_data = Url_Api.text

write_json = open('json_data.txt',mode='w',encoding='utf-8')
W_json = write_json.write(Json_data)
write_json.close()

with open('json_data.txt',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def Write_Data(data):
    
        for i in data:
                arrData = i +'\n'
                write_data = open("data.txt",mode='a+',encoding="utf-8")
                W_data = write_data.write(arrData)
                write_data.close() 
                print(arrData)

        return arrData



        