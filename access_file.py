import json
import requests

with open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\json\\json_file_test.json',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def Write_Data(data):

        for i in data:
                arrData = i +'\n'
                write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\html file\\data_test.html",mode='a+',encoding="utf-8")
                W_data = write_data.write(arrData)
                write_data.close() 
                print(arrData)

        return arrData

def show_Data_Brower(code_html):

        write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\html file\\data_test.html",mode='a+',encoding="utf-8")
        W_data = write_data.write(code_html)
        write_data.close() 

show_Data_Brower(code_html='''

<html style="text-align: center;background-color:#282828;">
    <head>
       <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <link rel="icon" href="C:\\Users\\clearlove7\\Documents\\GitHub\\App\\image\\logo.ico" type="image/gif/jpg/png/ico" sizes="50x50">
            <title>Data</title>
            <body>
            <div style="
                        color: white;
                        width: 200px;
                        height: 600px;
                        padding: 0;
                        margin: 0px auto;
                        display: inherit;
                        left: 5px;
                        position: relative;
                        overflow: auto;
                        top: 50px;
                
">
            <h1 style="position:fixed;
                        color: red;
                        font-family:arial;
                        text-align: center;
                        position: relative;
                        
    ">My Data
</h1>

''')

Write_Data(data=[
        str(value),
        str(value['id']),
        str(value['name']),
        str(value['email']),
        str(value['birthday']),
        str(value['gender']),
        str(value['age_range']),
        str(value['link']),
        str(value['name_format']),
        str(value['accounts']['data'][0]['access_token']),
        str(value['accounts']['data'][0]['category']),
        str(value['accounts']['data'][0]['category_list'][0]),
        str(value['accounts']['data'][0]['tasks']),
        str(value['accounts']['paging']['cursors']),
])



show_Data_Brower(code_html='''
        </div>
        </hr>
      </body>
   </head>
</html>

''')








































































        