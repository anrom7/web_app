import requests
import json
from urllib import request

url = "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=46201"
# open url the USDA’s API
url1 = request.urlopen(url)
print(type(url1))
content = url1.read().decode(url1.info().get_param('charset') or 'utf-8')
print(type(content))
data = json.loads(content)
print(type(data))
print(data)

# request to the USDA’s API
url2 = requests.get(url)
print(url2)
print(type(url2))
results = url2.json()
print(type(results))

for result in zip(data['results'],results['results']):
    assert result[0] == result[1]
    print(result[0])

