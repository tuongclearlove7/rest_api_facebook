import json
import requests


with open('C:\\Users\\clearlove7\\Documents\\GitHub\\App\\json\\json_file_test.json',mode='r',encoding='utf-8') as data_file:
        R_data = data_file.read()
value = json.loads(R_data)

def one_fields():
        global mydata
        fields1=str(input('input fields : '))
        print(value[fields1])
        mydata = str(value[fields1])


def two_fields():
        global mydata
        for i in value:
                print(i)
        fields1=str(input('input fields 1 : '))
        print(str(value[fields1]))

        print('________________________________________________________________________________________________________')
        
        fields2 = str(input('input fields 2 : '))
        print(value[fields1][fields2])
        mydata = str(value[fields1]) + str(value[fields1][fields2])


def three_fields():
        global mydata
        for i in value:
                print(i)
        while True:
              print("input has (fields has array) or no (fields no array)")
              option = input()
              fields1=str(input('input fields 1 : '))
              fields2 = str(input('input fields 2 : '))
              fields3 = str(input('input fields 3 : '))
              if(option=='has'):
                        print(str(value[fields1][fields2][0][fields3]))
                        mydata = str(value[fields1][fields2][0][fields3])
                        break;
              elif(option=='no'):
                        print(str(value[fields1][fields2][fields3]))
                        mydata = str(value[fields1][fields2][fields3])
                        break;
              elif(option != 'has' or 'no'):
                        print("You were inputing wrong option, please! re-enter")

def access_data():

        case = [None,'app1','app2','app3']

        while True:
                fields = input("input app : ")

                if fields == case[1]:
                        one_fields()
                        break;
                                
                elif fields == case[2]:
                        two_fields()
                        break;

                elif fields == case[3]:
                        three_fields()
                        break;

                if fields !=  case[1] or  case[2] :
                        print("You were inputing wrong fields, please! re-enter")

access_data()


def Write_Data(data):

                for i in data:
                        arrData = i +'\n'
                        write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\html file\\data_test.html",mode='a+',encoding="utf-8")
                        W_data = write_data.write(arrData)
                        write_data.close() 
                        print(arrData)

                return arrData

def outfile_html():
        write_data = open("C:\\Users\\clearlove7\\Documents\\GitHub\\App\\html file\\data_test.html",mode='a+',encoding="utf-8")
        W_data = write_data.write(mydata)
        write_data.close()


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

outfile_html()

show_Data_Brower(code_html='''

        </div>
        </hr>
        </body>
        </head>
        </html>

        ''')








































































        