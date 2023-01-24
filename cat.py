import requests
from requests.exceptions import HTTPError

url = 'http://numismatics.org/ocre/results?q=authority_facet%3A"Augustus"&lang=en'
response = requests.get(url)
a = response.text
print(type(a))
a = a.replace("<!DOCTYPE HTML>"," ")
print (a)
c = (a.find("h4"))
d = (a.find("h4",c+2))
b = ""
for i in range(d-c):
    b += a[i+c]
print (b)
a = a.replace(b," ")
c = (b.find("="))+2
d = (b.find("en"))+2
r = ""
for i in range(d-c):
    r += b[i+c]
r = "http://numismatics.org/ocre/"+r
print ("ссылка на монету =", r)
c = (b.find("en"))+4
d = (b.find("</"))
h = ""
for i in range(d-c):
    h += b[i+c]
print ("название монеты =", h)

c = (a.find("<dt>Date</dt>"))
d = (a.find("</dd></dl>",c))+4
b = ""
for i in range(d-c):
    b += a[i+c]

c = (b.find("dd"))+3
d = (b.find("</dd"))
data = ""
for i in range(d-c):
    data += b[i+c]
print ("датировка =", data)

c = (b.find("dd",d+4))+3
d = (b.find("</dd",c))
nomination = ""
for i in range(d-c):
    nomination += b[i+c]
print ("номинал =", nomination)

c = (b.find("dd",d+4))+3
d = (b.find("</dd",c))
monet_house = ""
for i in range(d-c):
    monet_house += b[i+c]
print ("Монетный двор =", monet_house)

c = (b.find("dd",d+4))+3
d = (b.find("</dd",c))
avers = ""
for i in range(d-c):
    avers += b[i+c]
print ("Аверс =", avers)

c = (b.find("dd",d+4))+3
d = (b.find("</dd",c))
revers = ""
for i in range(d-c):
    revers += b[i+c]
print ("Реверс =", revers)