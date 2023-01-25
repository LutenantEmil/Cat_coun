import requests
import time
from requests.exceptions import HTTPError

url = input("Введите сслыку для начала составления таблицы монет в виде: http://numismatics.org/ocre/results?q=authority_facet%3A""Augustus""&lang=en")
response = requests.get(url)
a = response.text
print(a)
c = (a.find("Displaying records"))+len("Displaying records")
d = (a.find("total",c))
b = ""
for i in range(d-c):
    b += a[i+c]
b = b.replace("\n","")
for i in range(len (b)):
    b = b.replace("  ", " ")
queue = b.split()
print("Общее число этих монет = ",queue[4])
dvadcatki = int(queue[4])//20
ostatok = int(queue[4])%20
print(dvadcatki)
print(ostatok)

for i in range(dvadcatki):
    #time.sleep(1)
    url = 'http://numismatics.org/ocre/results?q=authority_facet%3A"Augustus"&lang=en&start='+ str(20*i)
    response = requests.get(url)
    a = response.text
    for iterator in range(40):
        if iterator%2 == 0:
            c = (a.find("h4"))
            d = (a.find("h4", c + 2))
            b = ""
            for i in range(d - c):
                b += a[i + c]
            #print(b)
            c = (b.find("=")) + 2
            d = (b.find("en")) + 2
            monet_addres = ""
            for i in range(d - c):
                monet_addres += b[i + c]
            monet_addres = "http://numismatics.org/ocre/" + monet_addres
            print("ссылка на монету =", monet_addres)
            c = (b.find("en")) + 4
            d = (b.find("</"))
            monet_name = ""
            for i in range(d - c):
                monet_name += b[i + c]
            print("название монеты =", monet_name)
            if (a.find("<dt>Date</dt>")) < (a.find("<dt>Denomination</dt>")) and (a.find("<dt>Date</dt>")) > 0:
                c = (a.find("<dt>Date</dt>"))
                d = (a.find("</dd></dl>", c)) + 4
                b = ""
                for i in range(d - c):
                    b += a[i + c]
                #print(b)
                c = (b.find("dd")) + 3
                d = (b.find("</dd"))
                data = ""
                for i in range(d - c):
                    data += b[i + c]
                print("датировка =", data)
                data_digital = data.split()

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                nomination = ""
                for i in range(d - c):
                    nomination += b[i + c]
                print("номинал =", nomination)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                monet_house = ""
                for i in range(d - c):
                    monet_house += b[i + c]
                print("Монетный двор =", monet_house)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                avers = ""
                for i in range(d - c):
                    avers += b[i + c]
                print("Аверс =", avers)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                revers = ""
                for i in range(d - c):
                    revers += b[i + c]
                print("Реверс =", revers)
                a = a.replace(b," ",1)
            else:
                c = (a.find("<dt>Denomination</dt>"))
                d = (a.find("</dd></dl>", c)) + 4
                b = ""
                for i in range(d - c):
                    b += a[i + c]
                #print(b)
                print("датировка = не установлена")

                c = (b.find("dd")) + 3
                d = (b.find("</dd", c))
                nomination = ""
                for i in range(d - c):
                    nomination += b[i + c]
                print("номинал =", nomination)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                monet_house = ""
                for i in range(d - c):
                    monet_house += b[i + c]
                print("Монетный двор =", monet_house)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                avers = ""
                for i in range(d - c):
                    avers += b[i + c]
                print("Аверс =", avers)

                c = (b.find("dd", d + 4)) + 3
                d = (b.find("</dd", c))
                revers = ""
                for i in range(d - c):
                    revers += b[i + c]
                print("Реверс =", revers)
                a = a.replace(b, " ",1)
        else:
            c = (a.find("h4"))
            d = (a.find("h4", c + 2))+2
            b = ""
            for i in range(d - c):
                b += a[i + c]
            a = a.replace(b, " ",1)
            print("\n")

