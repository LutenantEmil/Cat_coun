import requests
from requests.exceptions import HTTPError
url = 'http://numismatics.org/ocre/results?q=denomination_facet%3A"Quinarius"+AND+authority_facet%3A"Augustus"+AND+mint_facet%3A"Emerita"&lang=en'
response = requests.get(url)
a = response.text
print(type(a))
a = a.replace("<!DOCTYPE HTML>"," ")
print (a)
c = (a.find("<dt>Date</dt>"))
b = ""
for i in range(1000):
    b += a[i+c]
print (b)