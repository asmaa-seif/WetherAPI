import requests , os
#Functions
def Get_pressure (dataRaw):
    maininfo = dataRaw['main']
    pressure = maininfo['pressure']
    print("The pressure is:", pressure)
    return str(pressure)
def Get_tempreture (dataRaw):
    tempreture = dataRaw['main']['temp']
    print("The tempreture is:",tempreture)
    return str(tempreture)
def Get_humiditiy (dataRaw):
    humidity = dataRaw['main']['humidity']
    print("the humidity is: ",humidity)
    return str(humidity)
def Get_Info(city,dataRaw):
   return'Our city is '+city+'\n' + 'The pressure is '+Get_pressure(dataRaw)+'\n'+'The tempreture is '+Get_tempreture(dataRaw)+'\n'+ 'The humedity is'+Get_humiditiy(dataRaw)+'\n'

flag = 0
while flag == 0:
    base = "https://api.openweathermap.org/data/2.5/weather?"
    print("enter new city or 1 to stop ")
    city = input()
    if city == '1':
        flag = 1
        print("thank you salam")
    elif city != '1':
        try:
            URL = base + "&q=" + city + "&appid=0888d6d73eeb6588a5b5da08f4d32bb9"
            r = requests.get(URL)
            dataRaw = r.json()
            f_wethear =open("D:\\wethear\\test.txt","a")
            f_wethear.write( str(Get_Info(city,dataRaw)) )
            f_wethear.close()
        except Exception as error:
            print(error)
