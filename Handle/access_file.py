import json
import requests

   



with open('json_file_test.json',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def Write_Data(data):
        for i in data:
                arrData = i +'\n'
                write_data = open("data_test.txt",mode='a+',encoding="utf-8")
                W_data = write_data.write(arrData)
                write_data.close() 
                print(arrData)

        return arrData



















        